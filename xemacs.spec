%define major 21
%define version %{major}.4.22
%define rversion %{major}.4.22
%define mversion %{major}.4
%define sumodate 2009-02-17
%define _requires_exceptions /bin/zsh /bin/csh

# force use of system malloc()
%define system_malloc_arches ppc64

%define release 8

Summary: Highly customizable text editor and application development system
Name: xemacs
Version: %{version}
Release: %{release}
License: GPLv2+
Group: Editors

Source0: ftp://ftp.xemacs.org/pub/xemacs/xemacs-%{mversion}/xemacs-%{rversion}.tar.bz2
Source1: ftp://ftp.xemacs.org/pub/xemacs/packages/xemacs-mule-sumo-%{sumodate}.tar.bz2
Source2: ftp://ftp.xemacs.org/pub/xemacs/packages/xemacs-sumo-%{sumodate}.tar.bz2
Source5: site-start-mdk.el
Source6: xemacs-16.png
Source7: xemacs-32.png
Source8: xemacs-48.png
Patch2: xemacs-21.4.22-non-x86-build.patch
Patch5: xemacs-21.4.9-fix-emacs-roots.patch
Patch6: xemacs-21.4.15-ppc64.patch
Patch10: xemacs-21.4.22-rpm-spec-mode.patch
Patch11: xemacs-21.4.21-lzma.patch

# Backport of patches:
#	http://cvs.fedoraproject.org/viewvc/rpms/xemacs/devel/xemacs-21.5.29-image-overflow.patch?revision=1.1
#	http://cvs.fedoraproject.org/viewvc/rpms/xemacs/devel/xemacs-21.5.29-png.patch?revision=1.1
Patch12: xemacs-21.4.22-CVE-2009-2688.patch

# http://tracker.xemacs.org/XEmacs/its/issue494 and #54215
Patch13: xemacs-21.4.22-ediff.patch

Provides: xemacs-noX xemacs-static xemacs-X11 xemacs-packages
Obsoletes: xemacs-noX xemacs-static xemacs-X11 xemacs-packages
Url: http://www.xemacs.org/
Buildroot: %{_tmppath}/xemacs-root
Requires: ctags
# It looks crap by default without these fonts - AdamW 2008/03, see
# http://forum.mandriva.com/viewtopic.php?p=457779
Suggests: x11-font-adobe-100dpi
BuildRequires:	Xaw3d-devel
BuildRequires:	autoconf2.1
BuildRequires:	bison
BuildRequires:	db-devel
BuildRequires:	compface-devel
BuildRequires:	lesstif-devel
BuildRequires:	ncurses-devel
BuildRequires:	libxml-devel
BuildRequires:	sendmail-command
BuildRequires:	xpm-devel
BuildRequires:  tiff-devel
BuildRequires:  jpeg-devel
BuildRequires:  png-devel
BuildRequires:	texinfo
BuildRequires:  x11-data-bitmaps
%ifarch alpha
BuildConflicts: compat-Tru64
%endif

Requires(preun): update-alternatives
Requires(post):  update-alternatives

%description 
XEmacs is a self-documenting, customizable, extensible, real-time
display editor. XEmacs is self-documenting because at any time you can
type in control-h to find out what your options are or to find out
what a command does. XEmacs is customizable because you can change the
definitions of XEmacs commands to anything you want. XEmacs is
extensible because you can write entirely new commands--programs in
the Lisp language to be run by Emacs' own Lisp interpreter. XEmacs
includes a real-time display, which means that the text being edited
is visible on the screen and is updated very frequently (usually after
every character or pair of characters) as you type.

To use XEmacs, you'll need to install the XEmacs binary. The xemacs package
includes the standard XEmacs binary that most people will use. The XEmacs
binary is dynamically linked, with both X11 and TTY (ncurses) support, but
without mule (MUlti-Lingual Emacs, the Asian character set) support.

%package devel
Summary: Header files for Xemacs
Group: Development/C
Requires: xemacs = %{version}
%description devel
Contains all the header files needed for xemacs development.

%package mule
Summary: The XEmacs binary with mule (MUlti-Lingual Emacs) support
Group: Editors
Requires: xemacs = %{version}
Provides: xemacs-mule-packages
Obsoletes: xemacs-mule-packages

Requires(preun): update-alternatives
Requires(post):  update-alternatives

%description mule
Xemacs-mule includes an XEmacs binary with support for
MUlti-Lingual Emacs and the Asian character set. Install xemacs-mule
(instead of xemacs) if you need to use Asian characters. Xemacs-mule is
compiled with X11 support only, so you won't be able to use it in a TTY
(ncurses) mode.

# %package gtk
# Summary: The XEmacs binary with GTK widgets
# Group: Editors
# Requires: xemacs = %{version}
# %description gtk
# XEmacs (and regular GNU Emacs, too) is a self-documenting, customizable,
# extensible, real-time display editor. XEmacs is self-documenting because at any
# time you can type in control-h to find out what your options are or to find out
# what a command does. XEmacs is customizable because you can change the
# definitions of XEmacs commands to anything you want. XEmacs is extensible
# because you can write entirely new commands--programs in the Lisp language to
# be run by Emacs' own Lisp interpreter. XEmacs includes a real-time display,
# which means that the text being edited is visible on the screen and is updated
# very frequently (usually after every character or pair of characters) as you
# type. This version used the GTK widgets

# %package gtk-gnome
# Summary: The XEmacs binary with GTK widgets
# Group: Editors
# Requires: xemacs = %{version}
# %description gtk-gnome
# XEmacs (and regular GNU Emacs, too) is a self-documenting, customizable,
# extensible, real-time display editor. XEmacs is self-documenting because at any
# time you can type in control-h to find out what your options are or to find out
# what a command does. XEmacs is customizable because you can change the
# definitions of XEmacs commands to anything you want. XEmacs is extensible
# because you can write entirely new commands--programs in the Lisp language to
# be run by Emacs' own Lisp interpreter. XEmacs includes a real-time display,
# which means that the text being edited is visible on the screen and is updated
# very frequently (usually after every character or pair of characters) as you
# type. This version used the GTK widgets and the gnome interface.


%package el
Summary: The .el source files for XEmacs
Group: Editors
Requires: xemacs = %{version}
%description el
Xemacs-el is not necessary to run XEmacs.  You'll only need to install
it if you're planning on incorporating some Lisp programming into your
XEmacs experience.

%package mule-el
Summary: The .el source files for XEmacs mule extension
Group: Editors
Requires: xemacs = %{version}
%description mule-el
Xemacs-el is not necessary to run XEmacs.  You'll only need to install
it if you're planning on incorporating some Lisp programming into your
XEmacs experience.

%package extras
Summary: Files that XEmacs has in common with GNU Emacs
Group: Editors
Requires: xemacs = %{version}
Provides: ctags
Conflicts: emacs

%description extras
Xemacs-extras includes files which are used by both GNU Emacs
and XEmacs. If you don't have GNU Emacs installed, be sure to also
install this package when you install the XEmacs text editor.

%prep
%setup -q

%ifnarch %{ix86}
%patch2 -p1
%endif

%patch5 -p1 -b .warly
%patch6 -p1 -b .ppc64
%patch11 -p1 -b .lzma
%patch12 -p1

%build

# done now not for xemacs to search packages file in future install root
rm -rf %{buildroot}

autoconf-2.13

rm -rf lisp/*.elc

rm -rf building && mkdir -p building && cd building

# standard: X11 and console support. No mule, though.
VAR_CONF="--prefix=/usr --exec-prefix=/usr --package-path=/%{_datadir}/xemacs/ --datadir=/%{_datadir} --mandir=/%{_mandir}/man0 --infodir=/%{_infodir} --libdir=/%{_libdir} --bindir=/%{_bindir} --infopath=/%{_infodir}"
XEMACS_CONFIG="$RPM_ARCH-mandrake-linux $VAR_CONF \
    --with-pop \
    --mail-locking=flock \
    --with-clash-detection \
    --with-scrollbars=lucid \
    --with-menubars=lucid \
    --with-dialogs=athena \
    --with-widgets=athena \
    --x-includes=%_includedir \
    --with-xpm \
    --with-xface \
    --with-png \
    --with-jpeg \
    --with-tiff \
    --dynamic=yes \
    --with-ncurses \
    --without-ldap \
    --without-postgresql \
    --with-clash-detection \
    --debug=no \
    --error-checking=none \
    --prefix=/usr \
    --exec-prefix=/usr \
    --with-x11 \
    --with-tty=yes \
    --with-athena=3d \
%ifarch %{system_malloc_arches}
    --with-system-malloc \
%endif
    --with-file-coding "
#	--with-meta-same-as-alt "
CFLAGS="$RPM_OPT_FLAGS"
export CFLAGS

# xemacs think // means ignore everything befor
RPM_BUILD_DIR=`echo $RPM_BUILD_DIR | sed "s,/\+,/,g"`
RPM_BUILD_ROOT=`echo %{buildroot} | sed "s,/\+,/,g"`
RPM_ARCH=%{_arch}
# FIXME local compilation with local path to compile file if xemacs is not installed on the compilation machine

{
rm -rf $RPM_ARCH-linux-local
mkdir $RPM_ARCH-linux-local
cd $RPM_ARCH-linux-local
../../configure $XEMACS_CONFIG --datadir=${RPM_BUILD_ROOT}%{_datadir} --package-path=${RPM_BUILD_ROOT}%{_datadir}/xemacs:${RPM_BUILD_DIR}/xemacs-%{version}/lisp
cd ..
}

{
rm -rf $RPM_ARCH-linux
mkdir $RPM_ARCH-linux
cd $RPM_ARCH-linux
../../configure $XEMACS_CONFIG --with-mule=no 
cd ..
}

# {
# rm -rf $RPM_ARCH-linux-gtk
# mkdir $RPM_ARCH-linux-gtk
# cd $RPM_ARCH-linux-gtk
# ../../configure $XEMACS_CONFIG --with-mule=no \
# 		--with-gtk
# cd ..
# }

# {
# rm -rf $RPM_ARCH-linux-gtk-gnome
# mkdir $RPM_ARCH-linux-gtk-gnome
# cd $RPM_ARCH-linux-gtk-gnome
# ../../configure $XEMACS_CONFIG --with-mule=no \
# 		--with-gtk \
# 		--with-gnome
# cd ..
# }

{
rm -rf $RPM_ARCH-linux-mule
mkdir $RPM_ARCH-linux-mule
cd $RPM_ARCH-linux-mule
../../configure $XEMACS_CONFIG --with-mule=yes \
		--with-xim=xlib
cd ..
}

{
pushd $RPM_ARCH-linux-local
make
popd
pushd $RPM_ARCH-linux 
make 
popd	
#  pushd $RPM_ARCH-linux-gtk && make && popd
#  pushd $RPM_ARCH-linux-gtk-gnome && make && popd
pushd $RPM_ARCH-linux-mule
make
popd
}
    
%install

# done again for short-circuit
rm -rf $RPM_BUILD_ROOT

pushd building/$RPM_ARCH-linux
%makeinstall mandir=$RPM_BUILD_ROOT/%{_mandir}/man1  lockdir=$RPM_BUILD_ROOT/var/lock/xemacs
popd

install -m 755 building/$RPM_ARCH-linux-mule/src/xemacs $RPM_BUILD_ROOT%{_bindir}/xemacs-mule
install -m 644 building/$RPM_ARCH-linux-mule/src/xemacs.dmp $RPM_BUILD_ROOT%{_bindir}/xemacs-mule.dmp
#install -m 755 building/$RPM_ARCH-linux-gtk/src/xemacs $RPM_BUILD_ROOT%{_bindir}/xemacs-gtk
#install -m 755 building/$RPM_ARCH-linux-gtk-gnome/src/xemacs $RPM_BUILD_ROOT%{_bindir}/xemacs-gtk-gnome
bzcat %{SOURCE1} | tar -xf - -C $RPM_BUILD_ROOT/%{_datadir}/xemacs
bzcat %{SOURCE2} | tar -xf - -C $RPM_BUILD_ROOT/%{_datadir}/xemacs
#bzcat %{SOURCE9} | tar -xf - -C $RPM_BUILD_ROOT/%{_datadir}/xemacs/xemacs-packages

pushd %{buildroot}
    patch -p1 < %{PATCH13}
    %{_builddir}/xemacs-%{version}/building/%{_arch}-linux-local/src/xemacs -batch -q -no-site-file -eval "(byte-compile-file \"%{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/ediff/ediff-init.el\")"
popd

rm -f $RPM_BUILD_ROOT/%{_datadir}/xemacs/xemacs-packages/lisp/hyperbole/file-newer

# this remove the usage of the AUTH command that breaks with most of the packages servers
perl -pi -e "s/\(defcustom efs-ftp-program-args '\(\"-i\" \"-n\" \"-g\" \"-v\"\)/(defcustom efs-ftp-program-args '(\"-i\" \"-n\" \"-g\" \"-v\" \"-u\")/" $RPM_BUILD_ROOT/%{_datadir}/xemacs/xemacs-packages/lisp/efs/efs.el
$RPM_BUILD_DIR/xemacs-%{version}/building/$RPM_ARCH-linux-local/src/xemacs -batch -q -no-site-file -eval "(byte-compile-file \"$RPM_BUILD_ROOT/%{_datadir}/xemacs/xemacs-packages/lisp/efs/efs.el\")"

# warly applied in sumo 2001 07 09
# pushd $RPM_BUILD_ROOT/%{_libdir}/xemacs/xemacs-packages && bzcat %{PATCH0} | patch -p1 && pushd $RPM_BUILD_ROOT/%{_libdir}/xemacs/xemacs-packages/lisp/mailcrypt/ && $RPM_BUILD_ROOT%{_bindir}/xemacs -batch -q -no-site-file -eval '(byte-compile-file "mc-gpg.el")' && popd && popd

# FIXME need to patch the rpm-spec-mode for short-circuit
pushd $RPM_BUILD_ROOT
cat %{PATCH10} | patch -p1
$RPM_BUILD_DIR/xemacs-%{version}/building/$RPM_ARCH-linux-local/src/xemacs -batch -q -no-site-file -eval "(byte-compile-file \"$RPM_BUILD_ROOT/%{_datadir}/xemacs/xemacs-packages/lisp/prog-modes/rpm-spec-mode.el\")"
popd

export specialel="_pkg.el hyperspec-carney.el ilisp-bug.el ilisp-cl-easy-menu.el mew-mule0.el mew-mule1.el mew-mule2.el mew-mule3.el eieio-tests.el hui-epV4-b.el erc-speak.el erc-chess.el url-riece.el un-trbase.el" 
for i in `find $RPM_BUILD_ROOT/%{_datadir}/xemacs/mule-packages/lisp/ $RPM_BUILD_ROOT/%{_datadir}/xemacs/xemacs-packages/lisp/ $RPM_BUILD_ROOT/%{_datadir}/xemacs/xemacs-%{version}/lisp/ \( -name "*.el" -or -name "*.elc" \) -a -not -name "*-skel.el" | perl -e 'while (<>) { /(.*\.el)$/ and push @doneel,$1; /(.*\.el)c$/ and $doneelc{$1} = 1 } foreach (split " ",$ENV{specialel}) { $doneelc{"$_"} = 1}; foreach (@doneel) { if (!$doneelc{"$_"} && (/([^\/]+)$/ and !$doneelc{$1})) { print "$_\n"}}'`;do pushd `echo $i | sed "s/\/[^\/]\+$//"` && $RPM_BUILD_DIR/xemacs-%{version}/building/$RPM_ARCH-linux-local/src/xemacs -batch -q -no-site-file -eval "(byte-compile-file \"$i\")";popd;done

mkdir -p $RPM_BUILD_ROOT/%{_infodir}/xemacs/mule
mv $RPM_BUILD_ROOT/%{_datadir}/xemacs/xemacs-packages/info/* $RPM_BUILD_ROOT/%{_infodir}/xemacs/
rmdir $RPM_BUILD_ROOT/%{_datadir}/xemacs/xemacs-packages/info/
mv $RPM_BUILD_ROOT/%{_datadir}/xemacs/mule-packages/info/* $RPM_BUILD_ROOT/%{_infodir}/xemacs/mule/
rmdir $RPM_BUILD_ROOT/%{_datadir}/xemacs/mule-packages/info/

find $RPM_BUILD_ROOT/%{_datadir}/xemacs/xemacs-packages -name \*.pl -exec \
perl -pi -e "s|/usr/local/bin/perl5|%{_bindir}/perl|g; \
		 s|/usr/local/bin/perl|%{_bindir}/perl|g;" {} \;

mkdir -p $RPM_BUILD_ROOT/etc/emacs/
install -m644 %{SOURCE5} $RPM_BUILD_ROOT/etc/emacs/site-start-xemacs.el
pushd $RPM_BUILD_ROOT/%{_datadir}/xemacs-%{version}/lisp/ && \
ln -s ../../../../etc/emacs/site-start-xemacs.el site-start.el && popd

mkdir $RPM_BUILD_ROOT%{_sysconfdir}/emacs/site-start.d

mkdir $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Xemacs
Comment=The XEmacs editor
Exec=%{_bindir}/%{name} %U
Icon=%{name}
Terminal=false
Type=Application
Categories=Motif;Utility;TextEditor;
EOF

for i in termcap.info-1 termcap.info-2 termcap.info-3 termcap.info info.info standards.info		 
do
  rm -f $RPM_BUILD_ROOT/%{_datadir}/info/$i
done

#mkdir $RPM_BUILD_ROOT%{_sysconfdir}/emacs/site-start.d

# Build file listings. (and make movemail setgid mail on RHL)
DIR="$RPM_BUILD_ROOT/%{_datadir}/xemacs-%{version}"
PACKAGES=$RPM_BUILD_ROOT/%{_datadir}/xemacs/xemacs-packages
LIBDIR="$RPM_BUILD_ROOT/%{_libdir}/xemacs-%{version}"
MULEDIR=$RPM_BUILD_ROOT/%{_datadir}/xemacs/mule-packages
INFO="*.info*"
EL="*.el"
DEVEL="-name *.h -o -name *.c -o -name Makefile"
NDEVEL="-not -name *.h -not -name *.c -not -name Makefile"
for i in $specialel version.el paths.el update-elc-2.el check-features.el
do
	NSPECIALEL="$NSPECIALEL -not -name $i"
	ANSPECIALEL="$ANSPECIALEL -and -not -name $i"
	SPECIALEL="$SPECIALEL -o -name $i"
done

chmod 644 $RPM_BUILD_ROOT/%{_datadir}/xemacs/xemacs-packages/lisp/edit-utils/info-look.el $RPM_BUILD_ROOT/%{_datadir}/xemacs/xemacs-packages/lisp/gnus/nnmail.el

# use update-alternatives
rm -f %{buildroot}%{_bindir}/%{name}
mv -f %{buildroot}%{_bindir}/{ctags,xemacs-ctags}

# 20060131 warly remove empty files
find $PACKAGES $MULEDIR -type f -name 'custom-load.el' -size 0 -delete

find $DIR $LIBDIR -type d -not -name "include" |
  sed -e "s#^$RPM_BUILD_ROOT#%dir #g" > rpm-files

find $PACKAGES -type d -not -name "include" |
  sed -e "s#^$RPM_BUILD_ROOT#%dir #g" > rpm-sumo-files

find $DIR $PACKAGES $LIBDIR $DEVEL -type f |
  sed -e "s#^$RPM_BUILD_ROOT##g" > rpm-devel-files

find $DIR $LIBDIR -name $EL -not -name "site-start.el" $ANSPECIALEL -type f |
  sed -e "s#^$RPM_BUILD_ROOT##g" > rpm-files

find $PACKAGES -name $EL -not -name "site-start.el" $ANSPECIALEL -type f |
  sed -e "s#^$RPM_BUILD_ROOT##g" > rpm-el-files

find $DIR $LIBDIR -not -name $INFO $NDEVEL -not -name $EL -type f |
  sed -e "
    s#^$RPM_BUILD_ROOT\(.*movemail\)#%attr(2755, root, mail) \1#g
    s#^$RPM_BUILD_ROOT##g
  " >> rpm-files

find $PACKAGES -not -name $INFO $NDEVEL -not -name $EL -type f |
  sed -e "
    s#^$RPM_BUILD_ROOT\(.*movemail\)#%attr(2755, root, mail) \1#g
    s#^$RPM_BUILD_ROOT##g
  " >> rpm-sumo-files

find $DIR $PACKAGES $LIBDIR -name "site-start.el" $SPECIALEL -type f |
  sed -e "
    s#^$RPM_BUILD_ROOT\(.*movemail\)#%attr(2755, root, mail) \1#g
    s#^$RPM_BUILD_ROOT##g
  " >> rpm-files

find $MULEDIR -type d -not -name "include" |
  sed -e "s#^$RPM_BUILD_ROOT#%dir #g" > rpm-mule-files

find $MULEDIR $NDEVEL -type f -not -name $EL |
 sed -e "s#^$RPM_BUILD_ROOT#%attr(-, root, root) #g" >> rpm-mule-files

find $MULEDIR $NDEVEL -type f -name $EL |
 sed -e "s#^$RPM_BUILD_ROOT#%attr(-, root, root) #g" >> rpm-mule-el-files

cat rpm-sumo-files >> rpm-files

install -m 644 -D %SOURCE6 %buildroot/%_iconsdir/hicolor/16x16/apps/xemacs.png
install -m 644 -D %SOURCE7 %buildroot/%_iconsdir/hicolor/32x32/apps/xemacs.png
install -m 644 -D %SOURCE8 %buildroot/%_iconsdir/hicolor/48x48/apps/xemacs.png

%post 
/usr/sbin/update-alternatives --install %{_bindir}/%{name} %{name} %{_bindir}/%{name}-%{version} %{major}
%if %mdkversion < 200900
%{update_menus}	
%{update_icon_cache hicolor}			
%endif

# euro only works in development version
#grep "Emacs\*font" || cat >> /usr/lib/X11/app-defaults/Emacs << EOF
#xemacs*font: -*-Fixed-Medium-R-*-*-*-130-*-*-*-*-iso8859-1
#EOF
cat %{_datadir}/xemacs-%{version}/etc/Emacs.ad >> /%{_sysconfdir}/X11/app-defaults/Emacs

for f in cl internals lispref texinfo xemacs custom emodules new-users-guide widget external-widget term xemacs-faq; do
  /sbin/install-info --section="XEmacs" %{_infodir}/$f.info%{_extension} %{_infodir}/dir
done
for f in %{_infodir}/xemacs/*.info%{_extension}; do
  /sbin/install-info --quiet --section="XEmacs" $f %{_infodir}/dir
done

%post extras
/usr/sbin/update-alternatives --install %{_bindir}/ctags ctags %{_bindir}/%{name}-ctags 0

%post mule
/usr/sbin/update-alternatives --install %{_bindir}/%{name} %{name} %{_bindir}/%{name}-mule %{major}
/usr/sbin/update-alternatives --set %{name} %{_bindir}/%{name}-mule
for f in %{_infodir}/xemacs/mule/*.info%{_extension}; do
   /sbin/install-info --quiet --section="XEmacs-mule" $f %{_infodir}/dir
done

%postun
[[ ! -f %{_bindir}/%{name}-%{version} ]] && \
    /usr/sbin/update-alternatives --remove %{name} %{_bindir}/%{name}-%{version} || :
%if %mdkversion < 200900
%{clean_menus}
%{clean_icon_cache hicolor}
%endif

%preun 
if [ "$1" = 0 ]; then
for f in cl internals lispref texinfo xemacs custom emodules new-users-guide widget external-widget term xemacs-faq; do
  /sbin/install-info --section="XEmacs" --delete %{_infodir}/$f.info%{_extension} %{_infodir}/dir
done
for f in %{_infodir}/xemacs/*.info%{_extension}; do
  [ -f $f ] && /sbin/install-info --quiet --section="XEmacs" --delete $f %{_infodir}/dir
done
fi

%preun mule
if [ "$1" = 0 ]; then
for f in %{_infodir}/xemacs/*.info%{_extension}; do
  [ -f $f ] && /sbin/install-info --quiet -section="XEmacs-mule" --delete $f %{_infodir}/dir
done
fi

%postun extras
[[ ! -f %{_bindir}/%{name}-ctags ]] && \
    /usr/sbin/update-alternatives --remove ctags %{_bindir}/%{name}-ctags || :

%postun mule
[[ ! -f %{_bindir}/%{name}-mule ]] && \
    /usr/sbin/update-alternatives --remove %{name} %{_bindir}/%{name}-mule || :

%files -f rpm-files
%defattr(-,root, root)
%doc BUGS ChangeLog README README.packages PROBLEMS
%config(noreplace) /etc/emacs/site-start-xemacs.el
%dir %{_sysconfdir}/emacs/site-start.d
%{_datadir}/applications/mandriva-xemacs.desktop
%{_bindir}/xemacs-%{version}*
%{_bindir}/gnuclient
%{_bindir}/gnuattach
%{_bindir}/ellcc
%{_bindir}/gnudoit
%{_mandir}/man1/xemacs.1*
%{_mandir}/man1/gnuserv.1*
%{_mandir}/man1/gnuclient.1*
%{_mandir}/man1/gnuattach.1*
%{_mandir}/man1/gnudoit.1*
%{_iconsdir}/hicolor/*/apps/*.png
%{_infodir}/*

%files devel -f rpm-devel-files
%defattr(-,root, root)
%{_datadir}/xemacs/mule-packages/etc/latin-unity/Makefile
%{_datadir}/xemacs/mule-packages/etc/mule-ucs/Makefile
%doc README

# 20060615 warly most of the basic xemacs menu function require a package anyway
# %files packages -f rpm-sumo-files
# %defattr(-,root, root)
# 
# 2005 warly this is not maintained
# %files gtk 
# %defattr(-,root, root)
# %{_bindir}/xemacs-gtk
# %doc README

# %files gtk-gnome 
# %defattr(-,root, root)
# %doc README
# %{_bindir}/xemacs-gtk-gnome

%files mule -f rpm-mule-files
%defattr(-,root, root)
%doc README
%{_bindir}/xemacs-mule*

#%files mule-packages -f rpm-mule-files
#%defattr(-,root, root)
#
%files el -f rpm-el-files
%defattr(-,root, root)
%doc README

%files mule-el -f rpm-mule-el-files
%defattr(-,root, root)
%doc README

%files extras
%defattr(-,root, root)
%doc README
%{_bindir}/b2m
%{_bindir}/etags
%{_bindir}/xemacs-ctags
%{_bindir}/ootags
%{_bindir}/rcs-checkin
%{_mandir}/man1/etags.1*
%{_mandir}/man1/ctags.1*

%clean
#rm -rf $RPM_BUILD_ROOT

