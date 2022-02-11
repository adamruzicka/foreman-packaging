%define debug_package %{nil}

%global go_arches x86_64 s390x ppc64le

Name:    yggdrasil
Version: 0.2.0
Release: 1%{?dist}
Summary: Message dispatch agent for cloud-connected systems
License: GPLv3
URL:     https://github.com/redhatinsights/yggdrasil

Source0: https://github.com/redhatinsights/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

Patch0:  Use-gzip-c-instead-of-k.patch
Patch1:  build-Remove-the-Makefile-preamble.patch

ExclusiveArch: %{go_arches}

BuildRequires: git
BuildRequires: golang
BuildRequires: dbus-devel
BuildRequires: systemd-devel

Requires: subscription-manager

%description
%{name} is pair of utilities that register systems with RHSM and establishes
a receiving queue for instructions to be sent to the system via a broker.

%prep
%autosetup -p1

%global ldflags %{expand:-linkmode=external -compressdwarf=false -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -extldflags '%__global_ldflags'}
%global buildflags %{expand:-compiler gc -buildmode pie -tags=\\"rpm_crashtraceback libtrust_openssl\\" -ldflags \\"%ldflags\\" -a -v -x %{?**}}

%build
CGO_CPPFLAGS="-D_FORTIFY_SOURCE=2 -fstack-protector-all"  \
BUILDFLAGS="%buildflags" \
make PREFIX=%{_prefix} \
     SYSCONFDIR=%{_sysconfdir} \
     LOCALSTATEDIR=%{_localstatedir} \
     SHORTNAME=%{name} \
     LONGNAME=%{name} \
     PKGNAME=%{name} \
     VERSION=%{version}

%install
CGO_CPPFLAGS="-D_FORTIFY_SOURCE=2 -fstack-protector-all"  \
BUILDFLAGS="%buildflags" \
make PREFIX=%{_prefix} \
     SYSCONFDIR=%{_sysconfdir} \
     LOCALSTATEDIR=%{_localstatedir} \
     DESTDIR=%{buildroot} \
     SHORTNAME=%{name} \
     LONGNAME=%{name} \
     PKGNAME=%{name} \
     VERSION=%{version} \
     install

%files
%doc README.md
%{_bindir}/%{name}
%{_sbindir}/%{name}d
%config(noreplace) %{_sysconfdir}/%{name}/config.toml
%{_unitdir}/%{name}d.service
%{_datadir}/bash-completion/completions/*
%{_mandir}/man1/*
%{_prefix}/share/pkgconfig/%{name}.pc
%{_libexecdir}/%{name}

%changelog
* Mon Oct 18 2021 Adam Ruzicka <aruzicka@redhat.com> - 0.2.0-1
- Initial release