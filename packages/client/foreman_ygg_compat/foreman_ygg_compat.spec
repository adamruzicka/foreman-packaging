%define debug_package %{nil}
%define worker_service com.redhat.Yggdrasil1.Worker1.foreman.service

%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

Name: foreman_ygg_compat
Version: 0.0.1
Summary: A compatibility layer for yggdrasil >=0.4.z
Release: 1%{?dist}
License: MIT

Source0: part-of-yggdrasild.service

Supplements: yggdrasil >= 0.4.0
Requires: yggdrasil >= 0.4.0

BuildRequires: systemd-rpm-macros

%description
A compatibility layer for yggdrasil >=0.4.z

%install
mkdir -p %{buildroot}%{_unitdir}
cat <<EOF >%{buildroot}%{_unitdir}/yggdrasild.service
[Service]
ExecStart=/bin/true

[Unit]
BindsTo=yggdrasil.service
BindsTo=%{worker_service}
EOF

install -Dp -m 644 %{SOURCE0} %{buildroot}%{_unitdir}/yggdrasil.service.d/foreman-override.conf
install -Dp -m 644 %{SOURCE0} %{buildroot}%{_unitdir}/%{worker_service}.d/foreman-override.conf

mkdir -p %{buildroot}%{_bindir}
ln -s %{_bindir}/yggd %{buildroot}%{_bindir}/yggdrasil

%post
if systemctl is-enabled yggdrasild >/dev/null; then
	sed -i 's/broker.*=/server =/' /etc/yggdrasil/config.toml
	echo 'prefix = "yggdrasil"' >>/etc/yggdrasil/config.toml
	echo 'data-host = ""' >>/etc/yggdrasil/config.toml
fi

%files
%{_unitdir}/yggdrasild.service
%{_unitdir}/yggdrasil.service.d/foreman-override.conf
%{_unitdir}/%{worker_service}.d/foreman-override.conf
%{_bindir}/yggdrasil

%changelog
* Thu Oct 03 2024 Adam Ruzicka <aruzicka@redhat.com> - 0.0.1-1
- Initial packaging
