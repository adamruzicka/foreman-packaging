# template: default
%global gem_name version_gem

Name: rubygem-%{gem_name}
Version: 1.1.3
Release: 1%{?dist}
Summary: Enhance your VERSION! Sugar for Version modules
License: MIT
URL: https://gitlab.com/oauth-xx/version_gem
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.2
BuildRequires: ruby >= 2.2
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Versions are good. Versions are cool. Versions will win.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/CODE_OF_CONDUCT.md
%license %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/SECURITY.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md

%changelog
* Wed Jul 19 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.1.3-1
- Update to 1.1.3

* Sun Mar 26 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.1.2-1
- Update to 1.1.2

* Sun Oct 02 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.1.1-1
- Update to 1.1.1

* Thu Aug 25 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.1.0-1
- Add rubygem-version_gem generated by gem2rpm using the default template

