%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-oslo
Version:        10.3.0
Release:        1%{?dist}
Summary:        Puppet module for managing Oslo.* library
License:        ASL 2.0

URL:            https://launchpad.net/puppet-oslo

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-inifile
Requires:       puppet-stdlib
Requires:       puppet-openstacklib
Requires:       puppet >= 2.7.0

%description
Puppet module for managing Oslo.* library

%prep
%setup -q -n openstack-oslo-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/oslo/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/oslo/



%files
%{_datadir}/openstack-puppet/modules/oslo/


%changelog
* Fri Feb 10 2017 Alfredo Moralejo <amoralej@redhat.com> 10.3.0-1
- Update to 10.3.0


