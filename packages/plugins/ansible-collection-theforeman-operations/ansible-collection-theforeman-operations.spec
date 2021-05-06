%global debug_package %{nil}

%global collection_namespace theforeman
%global collection_name operations
%global collection_directory %{_datadir}/ansible/collections/ansible_collections/%{collection_namespace}/%{collection_name}

%if 0%{?fedora} || 0%{?rhel} >= 8
%global ansible_python python3
%global pyyaml %{ansible_python}-pyyaml
%else
%global ansible_python python2
%global pyyaml PyYAML
%endif

%global release 1

Name:       ansible-collection-%{collection_namespace}-%{collection_name}
Version:    0.3.0
Release:    %{?prerelease:0.}%{release}%{?prerelease}%{?nightly}%{?dist}
Summary:    The Foreman Project Ansible operations collection

License:    GPLv3+
URL:        https://theforeman.org/plugins/foreman-operations-collection
Source0:    https://galaxy.ansible.com/download/%{collection_namespace}-%{collection_name}-%{version}.tar.gz
BuildArch:  noarch

Provides: ansible-collection(%{collection_namespace}.%{collection_name}) = %{version}
Requires: ansible >= 2.8

%description
Collection of Ansible Modules to manage Foreman installations.
Includes modules for Katello.

%prep
%setup -q -c

%build

%install
mkdir -p %{buildroot}%{collection_directory}
cp -a ./* %{buildroot}%{collection_directory}

%files
%{collection_directory}/
%license %{collection_directory}/LICENSE
%doc %{collection_directory}/README.md

%changelog
* Tue Apr 20 2021 Eric Helms - 0.3.0-1
- Initial package