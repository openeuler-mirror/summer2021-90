Name:           notepadqq
Version:        1.4.8
Release:        1%{?dist}
Summary:        An advanced text editor for developers
License:        GPLv3 
URL:            https://notepadqq.com/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         %{name}-add-node.patch
Patch2:         %{name}-appdata.patch

BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  qt5-linguist
BuildRequires:  qt5-devel
BuildRequires:  qtchooser
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       nodejs-shelljs
Requires:       mathjax
Requires:       hicolor-icon-theme

Provides:       bundled(nodejs-codemirror) = 5.33.0 
Provides:       bundled(nodejs-adm-zip)
Provides:       bundled(nodejs-archiver) = 0.14.4 
Provides:       bundled(jQuery) = 2.1.1
Provides:       bundled(requireJS) = 2.3.5

%description
A qt text editor for developers, with advanced tools, but remaining simple.
It supports syntax highlighting, themes and more

%prep
%autosetup -p1
rm -rf src/extension_tools/node_modules/shelljs
rm -rf src/editor/libs/MathJax
sed  -i -e '/cp -r libs\/MathJax/d' src/editor/Makefile

%build
export CXX=g++
export LDFLAGS="%{__global_ldflags}"
export CXXFLAGS="%{optflags}"
./configure --qmake=qmake-qt5 --lrelease %{_bindir}/lrelease-qt5
%make_build


%install
mkdir -p %{buildroot}%{_datadir}/%{name} \
         %{buildroot}%{_datadir}/applications \
         %{buildroot}%{_bindir} \
         %{buildroot}%{_mandir}/man1 \
         %{buildroot}%{_libexecdir}/%{name}/
install -pm 644 support_files/manpage/%{name}.1 %{buildroot}%{_mandir}/man1
desktop-file-install --remove-key=Encoding --remove-key=OnlyShowIn --remove-category=Utility \
 --dir=%{buildroot}%{_datadir}/applications support_files/shortcuts/%{name}.desktop
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 support_files/%{name}.appdata.xml %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
pushd out/release
install -pm 755 bin/* %{buildroot}%{_bindir}/
install -pm 755 lib/* %{buildroot}%{_libexecdir}/%{name}/
cp -a appdata/editor %{buildroot}%{_datadir}/%{name}/
cp -a appdata/extension_tools %{buildroot}%{_datadir}/%{name}/
ln -sf %{_bindir}/shjs %{buildroot}%{_datadir}/%{name}/extension_tools/node_modules/.bin/shjs
popd
find %{buildroot}%{_datadir} -name '*.sh' -exec chmod a+x {} ';'
find %{buildroot}%{_datadir} -name 'sauce.js' -exec chmod a+x {} ';'
find %{buildroot}%{_datadir} -name '.npmignore' -exec rm -rf {} ';'
for size in `ls support_files/icons/hicolor`; do
 mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${size}/apps
 install -pm 644 support_files/icons/hicolor/${size}/apps/%{name}.* %{buildroot}%{_datadir}/icons/hicolor/${size}/apps/
done

%files
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_libexecdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_metainfodir}/%{name}.appdata.xml
%license COPYING src/extension_tools/node_modules/archiver/LICENSE
%doc *.md



%changelog
* Mon Jul  6 2021 weiwei245 <weiqi_wang@126.com>      
- package init

