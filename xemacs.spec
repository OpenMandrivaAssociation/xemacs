%define major 21
%define rversion %{major}.4.22
%define mversion %{major}.4
%define sumodate 2009-02-17

%if %{_use_internal_dependency_generator}
%define __noautoreq '/bin/zsh|/bin/csh'
%else
%define _requires_exceptions /bin/zsh /bin/csh
%endif

Summary:	Highly customizable text editor and application development system
Name:		xemacs
Version:	%{major}.4.22
Release:	22
License:	GPLv2+
Group:		Editors
Url:		http://www.xemacs.org/
Source0:	ftp://ftp.xemacs.org/pub/xemacs/xemacs-%{mversion}/xemacs-%{rversion}.tar.bz2
Source1:	ftp://ftp.xemacs.org/pub/xemacs/packages/xemacs-mule-sumo-%{sumodate}.tar.bz2
Source2:	ftp://ftp.xemacs.org/pub/xemacs/packages/xemacs-sumo-%{sumodate}.tar.bz2
Source5:	site-start-mdk.el
Source6:	xemacs-16.png
Source7:	xemacs-32.png
Source8:	xemacs-48.png
Source9:	%{name}.rpmlintrc
Patch1:		xemacs-21.4.22-libpng15.patch
Patch2:		xemacs-21.4.22-non-x86-build.patch
Patch5:		xemacs-21.4.9-fix-emacs-roots.patch
Patch10:	xemacs-21.4.22-rpm-spec-mode.patch
Patch11:	xemacs-21.4.21-lzma.patch
# Backport of patches:
#	http://cvs.fedoraproject.org/viewvc/rpms/xemacs/devel/xemacs-21.5.29-image-overflow.patch?revision=1.1
#	http://cvs.fedoraproject.org/viewvc/rpms/xemacs/devel/xemacs-21.5.29-png.patch?revision=1.1
Patch12:	xemacs-21.4.22-CVE-2009-2688.patch
# http://tracker.xemacs.org/XEmacs/its/issue494 and #54215
Patch13:	xemacs-21.4.22-ediff.patch

Patch14: xemacs-21.4.22-texinfo5.1.patch
Patch15:	xemacs-21.4.22-gcc5.patch

Requires:	xemacs-extras
# It looks crap by default without these fonts - AdamW 2008/03, see
# http://forum.mandriva.com/viewtopic.php?p=457779
Suggests:	x11-font-adobe-100dpi
BuildRequires:	autoconf2.1
BuildRequires:	bison
BuildRequires:	texinfo
BuildRequires:	x11-data-bitmaps
BuildRequires:	compface-devel
BuildRequires:	db-devel
BuildRequires:	jpeg-devel
BuildRequires:	lesstif-devel
BuildRequires:	Xaw3d-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xpm)
Requires(preun,post):	update-alternatives

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

%files -f rpm-files
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

%post
/usr/sbin/update-alternatives --install %{_bindir}/%{name} %{name} %{_bindir}/%{name}-%{version} %{major}

cat %{_datadir}/xemacs-%{version}/etc/Emacs.ad >> /%{_sysconfdir}/X11/app-defaults/Emacs

%postun
[[ ! -f %{_bindir}/%{name}-%{version} ]] && \
    /usr/sbin/update-alternatives --remove %{name} %{_bindir}/%{name}-%{version} || :

#----------------------------------------------------------------------------

%package devel
Summary:	Header files for Xemacs
Group:		Development/C
Requires:	%{name} = %{EVRD}

%description devel
Contains all the header files needed for xemacs development.

%files devel -f rpm-devel-files
%{_datadir}/xemacs/mule-packages/etc/latin-unity/Makefile
%{_datadir}/xemacs/mule-packages/etc/mule-ucs/Makefile
%doc README

#----------------------------------------------------------------------------

%package mule
Summary:	The XEmacs binary with mule (MUlti-Lingual Emacs) support
Group:		Editors
Requires:	%{name} = %{EVRD}
Requires(preun,post):	update-alternatives

%description mule
Xemacs-mule includes an XEmacs binary with support for
MUlti-Lingual Emacs and the Asian character set. Install xemacs-mule
(instead of xemacs) if you need to use Asian characters. Xemacs-mule is
compiled with X11 support only, so you won't be able to use it in a TTY
(ncurses) mode.

%files mule -f rpm-mule-files
%doc README
%{_bindir}/xemacs-mule*

%post mule
/usr/sbin/update-alternatives --install %{_bindir}/%{name} %{name} %{_bindir}/%{name}-mule %{major}
/usr/sbin/update-alternatives --set %{name} %{_bindir}/%{name}-mule

%postun mule
[[ ! -f %{_bindir}/%{name}-mule ]] && \
    /usr/sbin/update-alternatives --remove %{name} %{_bindir}/%{name}-mule || :

#----------------------------------------------------------------------------

%package el
Summary:	The .el source files for XEmacs
Group:		Editors
Requires:	%{name} = %{EVRD}

%description el
Xemacs-el is not necessary to run XEmacs.  You'll only need to install
it if you're planning on incorporating some Lisp programming into your
XEmacs experience.

%files el -f rpm-el-files
%doc README

#----------------------------------------------------------------------------

%package mule-el
Summary:	The .el source files for XEmacs mule extension
Group:		Editors
Requires:	%{name} = %{EVRD}

%description mule-el
Xemacs-el is not necessary to run XEmacs.  You'll only need to install
it if you're planning on incorporating some Lisp programming into your
XEmacs experience.

%files mule-el -f rpm-mule-el-files
%doc README

#----------------------------------------------------------------------------

%package extras
Summary:	Files that XEmacs has in common with GNU Emacs
Group:		Editors
Requires:	%{name} = %{EVRD}

%description extras
Xemacs-extras includes files which are used by both GNU Emacs
and XEmacs. If you don't have GNU Emacs installed, be sure to also
install this package when you install the XEmacs text editor.

%files extras
%doc README
%{_bindir}/b2m
%{_bindir}/%{name}-etags
%{_bindir}/%{name}-ctags
%{_bindir}/ootags
%{_bindir}/rcs-checkin
%{_mandir}/man1/%{name}-etags.1*
%{_mandir}/man1/%{name}-ctags.1*

%post extras
/usr/sbin/update-alternatives --force --install %{_bindir}/ctags ctags %{_bindir}/%{name}-ctags 0
/usr/sbin/update-alternatives --force --install %{_bindir}/etags etags %{_bindir}/%{name}-etags 0

%postun extras
[[ ! -f %{_bindir}/%{name}-ctags ]] && \
    /usr/sbin/update-alternatives --remove ctags %{_bindir}/%{name}-ctags || :
[[ ! -f %{_bindir}/%{name}-etags ]] && \
    /usr/sbin/update-alternatives --remove etags %{_bindir}/%{name}-etags || :

#----------------------------------------------------------------------------

%prep
%setup -q

%ifnarch %{ix86}
%patch2 -p1
%endif

%patch5 -p1 -b .warly
%patch11 -p1 -b .lzma
%patch12 -p1
%patch1 -p1
%patch14 -p1
%patch15 -p1

%build
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
    --x-includes=%{_includedir} \
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
    --with-file-coding "

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

{
rm -rf %{_arch}-linux-mule
mkdir %{_arch}-linux-mule
cd %{_arch}-linux-mule
../../configure $XEMACS_CONFIG --with-mule=yes --with-xim=xlib
cd ..
}

{
pushd %{_arch}-linux-local
make
popd
pushd %{_arch}-linux
make
popd
pushd %{_arch}-linux-mule
make
popd
}

%install
pushd building/%{_arch}-linux
%makeinstall mandir=%{buildroot}%{_mandir}/man1  lockdir=%{buildroot}%{_var}/lock/xemacs
popd

install -m 755 building/%{_arch}-linux-mule/src/xemacs %{buildroot}%{_bindir}/xemacs-mule
install -m 644 building/%{_arch}-linux-mule/src/xemacs.dmp %{buildroot}%{_bindir}/xemacs-mule.dmp
bzcat %{SOURCE1} | tar -xf - -C %{buildroot}%{_datadir}/xemacs
bzcat %{SOURCE2} | tar -xf - -C %{buildroot}%{_datadir}/xemacs

pushd %{buildroot}
    patch -p1 < %{PATCH13}
    %{_builddir}/xemacs-%{version}/building/%{_arch}-linux-local/src/xemacs -batch -q -no-site-file -eval "(byte-compile-file \"%{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/ediff/ediff-init.el\")"
popd

rm -f %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/hyperbole/file-newer

# this remove the usage of the AUTH command that breaks with most of the packages servers
perl -pi -e "s/\(defcustom efs-ftp-program-args '\(\"-i\" \"-n\" \"-g\" \"-v\"\)/(defcustom efs-ftp-program-args '(\"-i\" \"-n\" \"-g\" \"-v\" \"-u\")/" %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/efs/efs.el
$RPM_BUILD_DIR/xemacs-%{version}/building/%{_arch}-linux-local/src/xemacs -batch -q -no-site-file -eval "(byte-compile-file \"%{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/efs/efs.el\")"

# FIXME need to patch the rpm-spec-mode for short-circuit
pushd %{buildroot}
cat %{PATCH10} | patch -p1
$RPM_BUILD_DIR/xemacs-%{version}/building/%{_arch}-linux-local/src/xemacs -batch -q -no-site-file -eval "(byte-compile-file \"%{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/prog-modes/rpm-spec-mode.el\")"
popd

export specialel="_pkg.el hyperspec-carney.el ilisp-bug.el ilisp-cl-easy-menu.el mew-mule0.el mew-mule1.el mew-mule2.el mew-mule3.el eieio-tests.el hui-epV4-b.el erc-speak.el erc-chess.el url-riece.el un-trbase.el" 
for i in `find %{buildroot}%{_datadir}/xemacs/mule-packages/lisp/ %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/ %{buildroot}%{_datadir}/xemacs/xemacs-%{version}/lisp/ \( -name "*.el" -or -name "*.elc" \) -a -not -name "*-skel.el" | perl -e 'while (<>) { /(.*\.el)$/ and push @doneel,$1; /(.*\.el)c$/ and $doneelc{$1} = 1 } foreach (split " ",$ENV{specialel}) { $doneelc{"$_"} = 1}; foreach (@doneel) { if (!$doneelc{"$_"} && (/([^\/]+)$/ and !$doneelc{$1})) { print "$_\n"}}'`;do pushd `echo $i | sed "s/\/[^\/]\+$//"` && $RPM_BUILD_DIR/xemacs-%{version}/building/%{_arch}-linux-local/src/xemacs -batch -q -no-site-file -eval "(byte-compile-file \"$i\")";popd;done

mkdir -p %{buildroot}%{_infodir}/xemacs/mule
mv %{buildroot}%{_datadir}/xemacs/xemacs-packages/info/* %{buildroot}%{_infodir}/xemacs/
rmdir %{buildroot}%{_datadir}/xemacs/xemacs-packages/info/
mv %{buildroot}%{_datadir}/xemacs/mule-packages/info/* %{buildroot}%{_infodir}/xemacs/mule/
rmdir %{buildroot}%{_datadir}/xemacs/mule-packages/info/

find %{buildroot}%{_datadir}/xemacs/xemacs-packages -name \*.pl -exec \
perl -pi -e "s|/usr/local/bin/perl5|%{_bindir}/perl|g; \
		 s|/usr/local/bin/perl|%{_bindir}/perl|g;" {} \;

mkdir -p %{buildroot}/etc/emacs/
install -m644 %{SOURCE5} %{buildroot}/etc/emacs/site-start-xemacs.el
pushd %{buildroot}%{_datadir}/xemacs-%{version}/lisp/ && \
ln -s ../../../../etc/emacs/site-start-xemacs.el site-start.el && popd

mkdir %{buildroot}%{_sysconfdir}/emacs/site-start.d

mkdir %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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
  rm -f %{buildroot}%{_datadir}/info/$i
done

# Build file listings. (and make movemail setgid mail on RHL)
DIR="%{buildroot}%{_datadir}/xemacs-%{version}"
PACKAGES=%{buildroot}%{_datadir}/xemacs/xemacs-packages
LIBDIR="%{buildroot}%{_libdir}/xemacs-%{version}"
MULEDIR=%{buildroot}%{_datadir}/xemacs/mule-packages
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

chmod 644 %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/edit-utils/info-look.el %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/gnus/nnmail.el

# use update-alternatives
rm -f %{buildroot}%{_bindir}/%{name}
mv -f %{buildroot}%{_bindir}/{ctags,xemacs-ctags}
mv -f %{buildroot}%{_bindir}/{etags,xemacs-etags}

# 20060131 warly remove empty files
find $PACKAGES $MULEDIR -type f -name 'custom-load.el' -size 0 -delete

find $DIR $LIBDIR -type d -not -name "include" |
  sed -e "s#^%{buildroot}#%dir #g" > rpm-files

find $PACKAGES -type d -not -name "include" |
  sed -e "s#^%{buildroot}#%dir #g" > rpm-sumo-files

find $DIR $PACKAGES $LIBDIR $DEVEL -type f |
  sed -e "s#^%{buildroot}##g" > rpm-devel-files

find $DIR $LIBDIR -name $EL -not -name "site-start.el" $ANSPECIALEL -type f |
  sed -e "s#^%{buildroot}##g" > rpm-files

find $PACKAGES -name $EL -not -name "site-start.el" $ANSPECIALEL -type f |
  sed -e "s#^%{buildroot}##g" > rpm-el-files

find $DIR $LIBDIR -not -name $INFO $NDEVEL -not -name $EL -type f |
  sed -e "
    s#^%{buildroot}\(.*movemail\)#%attr(2755, root, mail) \1#g
    s#^%{buildroot}##g
  " >> rpm-files

find $PACKAGES -not -name $INFO $NDEVEL -not -name $EL -type f |
  sed -e "
    s#^%{buildroot}\(.*movemail\)#%attr(2755, root, mail) \1#g
    s#^%{buildroot}##g
  " >> rpm-sumo-files

find $DIR $PACKAGES $LIBDIR -name "site-start.el" $SPECIALEL -type f |
  sed -e "
    s#^%{buildroot}\(.*movemail\)#%attr(2755, root, mail) \1#g
    s#^%{buildroot}##g
  " >> rpm-files

find $MULEDIR -type d -not -name "include" |
  sed -e "s#^%{buildroot}#%dir #g" > rpm-mule-files

find $MULEDIR $NDEVEL -type f -not -name $EL |
 sed -e "s#^%{buildroot}#%attr(-, root, root) #g" >> rpm-mule-files

find $MULEDIR $NDEVEL -type f -name $EL |
 sed -e "s#^%{buildroot}#%attr(-, root, root) #g" >> rpm-mule-el-files

cat rpm-sumo-files >> rpm-files

install -m 644 -D %{SOURCE6} %{buildroot}%{_iconsdir}/hicolor/16x16/apps/xemacs.png
install -m 644 -D %{SOURCE7} %{buildroot}%{_iconsdir}/hicolor/32x32/apps/xemacs.png
install -m 644 -D %{SOURCE8} %{buildroot}%{_iconsdir}/hicolor/48x48/apps/xemacs.png

mv %{buildroot}%{_mandir}/man1/ctags.1 %{buildroot}%{_mandir}/man1/%{name}-ctags.1
mv %{buildroot}%{_mandir}/man1/etags.1 %{buildroot}%{_mandir}/man1/%{name}-etags.1
mv %{buildroot}%{_infodir}/widget.info %{buildroot}%{_infodir}/%{name}-widget.info
mv %{buildroot}%{_infodir}/cl.info %{buildroot}%{_infodir}/%{name}-cl.info

