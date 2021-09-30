Name:           thonny
Version:        3.3.3
Release:        1
Summary:        Python IDE for beginners
License:        MIT 
URL:            https://thonny.org
Source0:        thonny-3.3.3.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-tkinter
BuildRequires:  python3-jedi
BuildRequires:  python3-pyserial
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  xorg-x11-server-Xvfb

Requires:       python3-tkinter
Requires:       python3-pip
Requires:       python3-mypy
Requires:       hicolor-icon-theme
Recommends:     python3-asttokens
Recommends:     python3-distro
Recommends:     zenity
Recommends:     xsel

%description
Thonny is a simple Python IDE with features useful for learning programming.
It comes with a debugger which is able to visualize all the conceptual steps
taken to run a Python program (executing statements, evaluating expressions,
maintaining the call stack). There is a GUI for installing 3rd party packages
and special mode for learning about references.

%prep
%autosetup -p1


%build
%py3_build

%install
%py3_install
install -m 0644 -D -T packaging/icons/thonny-256x256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-64x64.png   %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-48x48.png   %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-32x32.png   %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-22x22.png   %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-16x16.png   %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/thonny.png
install -D -m 0644 -t %{buildroot}%{_datadir}/metainfo                    packaging/linux/org.thonny.Thonny.appdata.xml
install -D -m 0644 -t %{buildroot}%{_mandir}/man1                         packaging/linux/thonny.1
desktop-file-install --dir=%{buildroot}%{_datadir}/applications           packaging/linux/org.thonny.Thonny.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.thonny.Thonny.appdata.xml


%check
xvfb-run py.test-3 --pyargs thonny

%files
%license LICENSE.txt licenses/ECLIPSE-ICONS-LICENSE.txt
%doc README.rst CHANGELOG.rst CREDITS.rst
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info/
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/thonny.png
%{_datadir}/applications/org.thonny.Thonny.desktop
%{_datadir}/metainfo/org.thonny.Thonny.appdata.xml
%{_mandir}/man1/thonny.1*



%changelog
* Thu Sep 30 2021 weiwei245 <weiqi_wang@126.com> - 3.3.3-1
- package init