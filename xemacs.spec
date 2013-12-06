%define major 21
%define version %{major}.4.22
%define rversion %{major}.4.22
%define mversion %{major}.4
%define sumodate 2009-02-17

%if %{_use_internal_dependency_generator}
%define __noautoreq '/bin/zsh|/bin/csh'
%else
%define _requires_exceptions /bin/zsh /bin/csh
%endif

# force use of system malloc()
%define system_malloc_arches ppc64

%define release 11

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
Source9: %{name}.rpmlintrc
Patch1: xemacs-21.4.22-libpng15.patch
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

Patch14: xemacs-21.4.22-texinfo5.1.patch

Provides: xemacs-noX xemacs-static xemacs-X11 xemacs-packages
Obsoletes: xemacs-noX xemacs-static xemacs-X11 xemacs-packages
Url: http://www.xemacs.org/
Buildroot: %{_tmppath}/xemacs-root
Requires: ctags
# It looks crap by default without these fonts - AdamW 2008/03, see
# http://forum.mandriva.com/viewtopic.php?p=457779
Suggests: x11-font-adobe-100dpi
BuildRequires:	Xaw3d-devel
BuildRequires:	xaw-devel
BuildRequires:	autoconf2.1
BuildRequires:	bison
BuildRequires:	db-devel
BuildRequires:	compface-devel
BuildRequires:	lesstif-devel
BuildRequires:	ncurses-devel
#BuildRequires:	sendmail-command
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
%patch1 -p1
%patch14 -p1

%build

# done now not for xemacs to search packages file in future install root
rm -rf %{buildroot}

autoreconf-2.13 -i

rm -rf lisp/*.elc

rm -rf building && mkdir -p building && cd building

# standard: X11 and console support. No mule, though.
VAR_CONF="--prefix=/usr --exec-prefix=/usr --package-path=/%{_datadir}/xemacs/ --datadir=/%{_datadir} --mandir=/%{_mandir}/man0 --infodir=/%{_infodir} --libdir=/%{_libdir} --bindir=/%{_bindir} --infopath=/%{_infodir}"
XEMACS_CONFIG="%{_arch}-mandriva-linux $VAR_CONF \
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
#CFLAGS="$RPM_OPT_FLAGS"
#export CFLAGS

# xemacs think // means ignore everything befor
RPM_BUILD_DIR=`echo $RPM_BUILD_DIR | sed "s,/\+,/,g"`
RPM_BUILD_ROOT=`echo %{buildroot} | sed "s,/\+,/,g"`
# FIXME local compilation with local path to compile file if xemacs is not installed on the compilation machine

{
rm -rf %{_arch}-linux-local
mkdir %{_arch}-linux-local
cd %{_arch}-linux-local
../../configure $XEMACS_CONFIG --datadir=${RPM_BUILD_ROOT}%{_datadir} --package-path=${RPM_BUILD_ROOT}%{_datadir}/xemacs:${RPM_BUILD_DIR}/xemacs-%{version}/lisp
cd ..
}

{
rm -rf %{_arch}-linux
mkdir %{_arch}-linux
cd %{_arch}-linux
../../configure $XEMACS_CONFIG --with-mule=no 
cd ..
}

# {
# rm -rf %{_arch}-linux-gtk
# mkdir %{_arch}-linux-gtk
# cd %{_arch}-linux-gtk
# ../../configure $XEMACS_CONFIG --with-mule=no \
# 		--with-gtk
# cd ..
# }

# {
# rm -rf %{_arch}-linux-gtk-gnome
# mkdir %{_arch}-linux-gtk-gnome
# cd %{_arch}-linux-gtk-gnome
# ../../configure $XEMACS_CONFIG --with-mule=no \
# 		--with-gtk \
# 		--with-gnome
# cd ..
# }

{
rm -rf %{_arch}-linux-mule
mkdir %{_arch}-linux-mule
cd %{_arch}-linux-mule
../../configure $XEMACS_CONFIG --with-mule=yes \
		--with-xim=xlib
cd ..
}

{
pushd %{_arch}-linux-local
make
popd
pushd %{_arch}-linux 
make 
popd	
#  pushd %{_arch}-linux-gtk && make && popd
#  pushd %{_arch}-linux-gtk-gnome && make && popd
pushd %{_arch}-linux-mule
make
popd
}
    
%install

# done again for short-circuit
rm -rf $RPM_BUILD_ROOT

pushd building/%{_arch}-linux
%makeinstall mandir=$RPM_BUILD_ROOT/%{_mandir}/man1  lockdir=$RPM_BUILD_ROOT/var/lock/xemacs
popd

install -m 755 building/%{_arch}-linux-mule/src/xemacs $RPM_BUILD_ROOT%{_bindir}/xemacs-mule
install -m 644 building/%{_arch}-linux-mule/src/xemacs.dmp $RPM_BUILD_ROOT%{_bindir}/xemacs-mule.dmp
#install -m 755 building/%{_arch}-linux-gtk/src/xemacs $RPM_BUILD_ROOT%{_bindir}/xemacs-gtk
#install -m 755 building/%{_arch}-linux-gtk-gnome/src/xemacs $RPM_BUILD_ROOT%{_bindir}/xemacs-gtk-gnome
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
$RPM_BUILD_DIR/xemacs-%{version}/building/%{_arch}-linux-local/src/xemacs -batch -q -no-site-file -eval "(byte-compile-file \"$RPM_BUILD_ROOT/%{_datadir}/xemacs/xemacs-packages/lisp/efs/efs.el\")"

# warly applied in sumo 2001 07 09
# pushd $RPM_BUILD_ROOT/%{_libdir}/xemacs/xemacs-packages && bzcat %{PATCH0} | patch -p1 && pushd $RPM_BUILD_ROOT/%{_libdir}/xemacs/xemacs-packages/lisp/mailcrypt/ && $RPM_BUILD_ROOT%{_bindir}/xemacs -batch -q -no-site-file -eval '(byte-compile-file "mc-gpg.el")' && popd && popd

# FIXME need to patch the rpm-spec-mode for short-circuit
pushd $RPM_BUILD_ROOT
cat %{PATCH10} | patch -p1
$RPM_BUILD_DIR/xemacs-%{version}/building/%{_arch}-linux-local/src/xemacs -batch -q -no-site-file -eval "(byte-compile-file \"$RPM_BUILD_ROOT/%{_datadir}/xemacs/xemacs-packages/lisp/prog-modes/rpm-spec-mode.el\")"
popd

export specialel="_pkg.el hyperspec-carney.el ilisp-bug.el ilisp-cl-easy-menu.el mew-mule0.el mew-mule1.el mew-mule2.el mew-mule3.el eieio-tests.el hui-epV4-b.el erc-speak.el erc-chess.el url-riece.el un-trbase.el" 
for i in `find $RPM_BUILD_ROOT/%{_datadir}/xemacs/mule-packages/lisp/ $RPM_BUILD_ROOT/%{_datadir}/xemacs/xemacs-packages/lisp/ $RPM_BUILD_ROOT/%{_datadir}/xemacs/xemacs-%{version}/lisp/ \( -name "*.el" -or -name "*.elc" \) -a -not -name "*-skel.el" | perl -e 'while (<>) { /(.*\.el)$/ and push @doneel,$1; /(.*\.el)c$/ and $doneelc{$1} = 1 } foreach (split " ",$ENV{specialel}) { $doneelc{"$_"} = 1}; foreach (@doneel) { if (!$doneelc{"$_"} && (/([^\/]+)$/ and !$doneelc{$1})) { print "$_\n"}}'`;do pushd `echo $i | sed "s/\/[^\/]\+$//"` && $RPM_BUILD_DIR/xemacs-%{version}/building/%{_arch}-linux-local/src/xemacs -batch -q -no-site-file -eval "(byte-compile-file \"$i\")";popd;done

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

for i in termcap.info-1 termcap.info-2 termcap.info-3 termcap.info info.info \
    standards.info cl.info widget.info
do
  rm -f $RPM_BUILD_ROOT/%{_datadir}/info/$i
done
  rm -f $RPM_BUILD_ROOT/%{_datadir}/info/texinfo.info*

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

# euro only works in development version
#grep "Emacs\*font" || cat >> /usr/lib/X11/app-defaults/Emacs << EOF
#xemacs*font: -*-Fixed-Medium-R-*-*-*-130-*-*-*-*-iso8859-1
#EOF
cat %{_datadir}/xemacs-%{version}/etc/Emacs.ad >> /%{_sysconfdir}/X11/app-defaults/Emacs


%post extras
/usr/sbin/update-alternatives --install %{_bindir}/ctags ctags %{_bindir}/%{name}-ctags 0

%post mule
/usr/sbin/update-alternatives --install %{_bindir}/%{name} %{name} %{_bindir}/%{name}-mule %{major}
/usr/sbin/update-alternatives --set %{name} %{_bindir}/%{name}-mule

%postun
[[ ! -f %{_bindir}/%{name}-%{version} ]] && \
    /usr/sbin/update-alternatives --remove %{name} %{_bindir}/%{name}-%{version} || :

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



%changelog
* Wed May 16 2012 Crispin Boylan <crisb@mandriva.org> 21.4.22-8
+ Revision: 799234
- Fix hang on x86_64
- Patch1 (from mageia) - Fix build with latest libpng
- Rebuild

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 21.4.22-7mdv2011.0
+ Revision: 615530
- the mass rebuild of 2010.1 packages

* Sat Jan 16 2010 Funda Wang <fwang@mandriva.org> 21.4.22-6mdv2010.1
+ Revision: 492269
- rebuild for new libjpeg v8

* Thu Dec 31 2009 Funda Wang <fwang@mandriva.org> 21.4.22-5mdv2010.1
+ Revision: 484300
- BR compface
- rebuild for db 4.8

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Use update-alternatives for xemacs ctags

* Mon Oct 05 2009 Paulo Andrade <pcpa@mandriva.com.br> 21.4.22-3mdv2010.0
+ Revision: 454266
- Use update alternatives to correct problems when xemacs-mule is installed.

* Fri Oct 02 2009 Paulo Andrade <pcpa@mandriva.com.br> 21.4.22-2mdv2010.0
+ Revision: 452404
- correct broken ediff output (http://tracker.xemacs.org/XEmacs/its/issue494)

* Sat Sep 26 2009 Paulo Andrade <pcpa@mandriva.com.br> 21.4.22-1mdv2010.0
+ Revision: 449348
- Update to latest stable release 21.4.22
- Update mule-sumo to 2009-02-17
- Add correction for CVE-2009-2688

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 21.4.21-9mdv2009.0
+ Revision: 262310
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 21.4.21-8mdv2009.0
+ Revision: 256785
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Mar 26 2008 Adam Williamson <awilliamson@mandriva.org> 21.4.21-6mdv2008.1
+ Revision: 190192
- suggest x11-font-adobe-100dpi (without these fonts, it looks rather bad by default)

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 21.4.21-5mdv2008.1
+ Revision: 171183
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix gstreamer0.10-devel BR for x86_64
- fix summary-ended-with-dot
- fix spacing at top of description

* Fri Jan 18 2008 Adam Williamson <awilliamson@mandriva.org> 21.4.21-4mdv2008.1
+ Revision: 154978
- add lzma.patch to fix #36961 (can't open lzma-compressed info files)

* Sun Dec 30 2007 Adam Williamson <awilliamson@mandriva.org> 21.4.21-3mdv2008.1
+ Revision: 139480
- fixes from Shlomi Fish: don't needlessly auto-require tcsh, add missing %% to several uses of %%{_extension}

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 09 2007 Funda Wang <fwang@mandriva.org> 21.4.21-2mdv2008.1
+ Revision: 116647
- fix comment of desktop item

* Sun Dec 09 2007 Funda Wang <fwang@mandriva.org> 21.4.21-1mdv2008.1
+ Revision: 116611
- New version 21.4.21

* Thu Dec 06 2007 Adam Williamson <awilliamson@mandriva.org> 21.4.20-4mdv2008.1
+ Revision: 116077
- fix hardcoded extension for info files (#35965)

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-ended-with-dot
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Sat Jul 21 2007 Adam Williamson <awilliamson@mandriva.org> 21.4.20-3mdv2008.0
+ Revision: 54103
- rebuild against new lesstif
- improve xdg menu
- fd.o icons
- buildrequires autoconf2.1 (2.1 is no longer the default)

* Thu May 31 2007 Funda Wang <fwang@mandriva.org> 21.4.20-2mdv2008.0
+ Revision: 33003
- kill old menu
  fix post script

* Tue May 29 2007 Funda Wang <fwang@mandriva.org> 21.4.20-1mdv2008.0
+ Revision: 32336
- New version of sumo
- New version

