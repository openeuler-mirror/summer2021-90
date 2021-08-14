%global geany_docdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}
%undefine  py_auto_byte_compile

Name:      geany
Version:   1.37.1
Release:   1%{?dist}
Summary:   A fast and lightweight IDE using GTK3
License:   GPLv2+ and MIT
URL:       http://www.geany.org/
Source0:   http://download.geany.org/%{name}-%{version}.tar.bz2
Patch0:    %{name}-gcc.patch

BuildRequires: gcc gcc-c++
BuildRequires: python3-docutils
BuildRequires: desktop-file-utils, gettext, pango-devel, intltool
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: perl(XML::Parser)
BuildRequires: make

Requires: vte291%{?_isa}
Requires: geany-libgeany = %{version}-%{release}

Provides: bundled(scintilla) = 3.10.4

Recommends: xterm


%description
Geany is a small and fast integrated development environment with basic
features and few dependencies to other packages or Desktop Environments.




%package libgeany
Summary:   Core functions of Geany


%description libgeany
This package contains the core functions of Geany which will be used by
Geany plugins.


%package devel
Summary:   Header files for building Geany plug-ins
Requires:  geany = %{version}-%{release}
Requires:  pkgconfig gtk3-devel

%description devel
This package contains the header files and pkg-config file needed for building
Geany plug-ins. You do not need to install this package to use Geany.

%prep
%setup -q
%patch0 -p1
rm -f waf
rm -f wscript


%build
RST2HTML=/usr/bin/rst2html-3
%configure --docdir=%{geany_docdir} --enable-gtk3
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT DOCDIR=$RPM_BUILD_ROOT/%{geany_docdir}
rm -f $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.ico
desktop-file-install --delete-original \
        --dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
        --mode 0644                                             \
        $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
find $RPM_BUILD_ROOT -name "*.la" -delete
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
BugReportURL: https://sourceforge.net/p/geany/feature-requests/739/
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">geany.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <description>
    <p>
      Geany is a small and lightweight Integrated Development Environment.
      It was developed to provide a small and fast IDE.
      Another goal was to be as independent as possible from a KDE or GNOME -
      Geany only requires the GTK3 runtime libraries.
    </p>
  <!-- FIXME: Probably needs another paragraph or two -->
  </description>
  <url type="homepage">http://www.geany.org/</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/geany/a.png</screenshot>
    <screenshot>https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/geany/b.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%files -f %{name}.lang
%exclude %{geany_docdir}/TODO
%doc %{geany_docdir}
%doc %{_mandir}/man1/geany.1*
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*/*/*/*.svg
%{_datadir}/icons/*/*/*/*.png
%files libgeany
%{_libdir}/libgeany.so*
%files devel
%doc HACKING TODO
%{_includedir}/geany
%{_libdir}/pkgconfig/geany.pc


%changelog
* Mon Jul  6 2021 weiwei245 <weiqi_wang@126.com>      
- package init
