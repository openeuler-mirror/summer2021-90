Name:           python-jedi
Version:        0.18.0
Release:        1
Summary:        An auto completion tool for Python that can be used for text editors

License:        MIT and ASL 2.0

%global django_stubs_commit fd057010f6cbf176f57d1099e82be46d39b99cb9
%global typeshed_commit     d38645247816f862cafeed21a8f4466d306aacf3
URL:            https://jedi.readthedocs.org
Source0:        https://github.com/davidhalter/jedi/archive/v%{version}/jedi-%{version}.tar.gz
Source1:        https://github.com/davidhalter/django-stubs/archive/%{django_stubs_commit}/django-stubs-%{django_stubs_commit}.tar.gz
Source2:        https://github.com/davidhalter/typeshed/archive/%{typeshed_commit}/typeshed-%{typeshed_commit}.tar.gz
BuildArch:      noarch
Patch0:         py3_inspect_fix.patch



%global common_description %{expand:
Jedi is a static analysis tool for Python that can be used in IDEs/editors. Its
historic focus is autocompletion, but does static analysis for now as well.
Jedi is fast and is very well tested. It understands Python on a deeper level
than all other static analysis frameworks for Python.}

%description %{common_description}


%package -n python3-jedi
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-jedi}
Provides:       bundled(python3dist(django-stubs)) = %{django_stubs_commit}
Provides:       bundled(typeshed) = %{typeshed_commit}
%description -n python3-jedi %{common_description}




%prep
%autosetup -n jedi-%{version} -p 1
pushd jedi/third_party
rmdir django-stubs typeshed
tar xf %{SOURCE1} && mv django-stubs-%{django_stubs_commit} django-stubs
tar xf %{SOURCE2} && mv typeshed-%{typeshed_commit} typeshed
popd
cp -p jedi/third_party/django-stubs/LICENSE.txt LICENSE-django-stubs.txt
cp -p jedi/third_party/typeshed/LICENSE LICENSE-typeshed.txt


%build
%py3_build


%install
%py3_install



%files -n python3-jedi
%license LICENSE.txt LICENSE-django-stubs.txt LICENSE-typeshed.txt
%doc AUTHORS.txt CHANGELOG.rst README.rst
%{python3_sitelib}/jedi/
%{python3_sitelib}/jedi-%{version}-py%{python3_version}.egg-info/


%changelog
* Thu Sep 30 2021 weiwei245 <weiqi_wang@126.com> - 0.18.0-1
- package init

