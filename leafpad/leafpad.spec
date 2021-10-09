
Name:           leafpad
Version:        0.8.18.1
Release:        1

Summary:        GTK+ based simple text editor
License:        GPLv2+
URL:            http://tarot.freeshell.org/leafpad/
Source0:        http://savannah.nongnu.org/download/leafpad/%{name}-%{version}.tar.gz
Patch0:         01-gcc-format.patch

BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel >= 2.4
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires: make

%description
Leafpad is a GTK+ based simple text editor. The user interface is similar to
Notepad. It aims to be lighter than GEdit and KWrite, and to be as useful as
them.


%prep
%setup -q
sed -i 's/g_strcasecmp/g_ascii_strcasecmp/g' src/main.c
sed -i 's/g_strcasecmp/g_ascii_strcasecmp/g' src/dnd.c
sed -i 's/g_strcasecmp/g_ascii_strcasecmp/g' src/selector.c
%patch0

%build
%configure --enable-chooser

%make_build


%install
%make_install

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/leafpad.desktop

%find_lang %{name}


%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/pixmaps/leafpad.*

%changelog
* Thu Sep 30 2021 weiwei245 <weiqi_wang@126.com> - 0.8.18-1
- package init
