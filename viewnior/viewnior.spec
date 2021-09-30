Name:           viewnior
Version:        1.7
Release:        1
Summary:        Elegant image viewer

License:        GPLv3+
URL:            http://siyanpanayotov.com/project/viewnior/
Source0:        https://github.com/hellosiyan/Viewnior/archive/%{name}-%{version}.tar.gz
Patch0:         fix-appdata.patch

BuildRequires:  pkgconfig(gtk+-2.0) >= 2.20
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gio-2.0) >= 2.32
BuildRequires:  pkgconfig(shared-mime-info) >= 0.20
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.4.0
BuildRequires:  pkgconfig(exiv2) >= 0.21
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  gnome-common
BuildRequires:  gcc-c++

%description 
Viewnior is an image viewer program. Created to be simple, fast and elegant. 
It's minimalistic interface provides more screen space for your images. 


%prep
%autosetup -n Viewnior-%{name}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS TODO
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}/
%{_mandir}/man*/%{name}*



%changelog
* Thu Sep 30 2021 weiwei245 <weiqi_wang@126.com> - 1.7-1
- package init
