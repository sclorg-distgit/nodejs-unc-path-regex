%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global npm_name unc-path-regex

Summary:       Test if a file path is a windows UNC file path
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       0.1.1
Release:       3%{?dist}
License:       MIT
URL:           https://github.com/jonschlinkert/unc-path-regex
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs010-runtime
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
Regular expression for testing if a file path is a 
windows UNC file path. Can also be used as a component 
of another regexp via the .source property.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%files
%doc README.md LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.1-3
- rebuilt

* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 0.1.1-2
- Enable scl macros

* Tue Nov 17 2015 Troy Dawson <tdawson@redhat.com> - 0.1.1-1
- Initial package
