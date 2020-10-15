# Generated from pulp_file_client-0.0.1b10.dev.1557779852.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name pulp_file_client

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.3.0
Release: 1%{?dist}
Summary: Pulp 3 API Ruby Gem
Group: Development/Languages
License: GPLv2
URL: https://openapi-generator.tech
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 1.9
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(faraday) >= 0.14.0
Requires: %{?scl_prefix_ruby}rubygem(json) >= 2.1.0
Requires: %{?scl_prefix_ruby}rubygem(json) >= 2.1
Requires: %{?scl_prefix_ruby}rubygem(json) < 3
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 1.9
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
Pulp3 file plugin api library.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

rm %{buildroot}/%{gem_instdir}/git_push.sh

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/docs
%{gem_instdir}/pulp_file_client.gemspec
%{gem_instdir}/spec

%changelog
* Thu Oct 15 2020 ianballou <ianballou67@gmail.com> 1.3.0-1
- Update to 1.3.0

* Thu Aug 20 2020 Justin Sherrill <jsherril@redhat.com> 1.2.0-1
- Update to 1.2.0

* Mon Jun 08 2020 James Jeffers 1.0.1-1
- Update to 1.0.1

* Mon May 04 2020 Justin Sherrill <jsherril@redhat.com> 0.3.0-1
- Update to 0.3.0

* Thu Mar 26 2020 Samir Jha <sjha4@ncsu.edu> 0.2.0-1
- Update to 0.2.0

* Mon Jan 06 2020 Justin Sherrill <jsherril@redhat.com> 0.1.0-1
- Update to 0.1.0

* Mon Nov 04 2019 Justin Sherrill <jsherril@redhat.com> 0.1.0b5.dev01571253617-1
- Update to a newer release

* Mon Jun 10 2019 Justin Sherrill <jlsherrill@gmail.com> 3.0.0rc2.dev.1558441126-1
- Update to a recent rc2 release

* Mon May 13 2019 Justin Sherrill <jlsherrill@gmail.com> 0.0.1b10.dev.1557779852-1
- Add rubygem-pulpcore_client generated by gem2rpm using the scl template

