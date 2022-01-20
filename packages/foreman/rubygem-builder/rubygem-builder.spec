# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name builder

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.2.4
Release: 2%{?dist}
Summary: Builders for MarkUp
Group: Development/Languages
License: MIT
URL: http://onestepback.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

Obsoletes: tfm-ror52-rubygem-%{gem_name} <= 3.2.3

%description
Builder provides a number of builder objects that make creating structured
data
simple to do.  Currently the following builder objects are supported:
* XML Markup
* XML Events.


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
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%{gem_instdir}/rakelib
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/builder.blurb
%exclude %{gem_instdir}/builder.gemspec

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGES
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/doc
%{gem_instdir}/test

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.2.4-2
- Rebuild against rh-ruby27

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.2.4-1
- Release rubygem-builder 3.2.4

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.2.3-4
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.2.3-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 3.2.3-2
- Bump for moving over to foreman-packaging

* Thu Jul 19 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.2.3-1
- Initial package