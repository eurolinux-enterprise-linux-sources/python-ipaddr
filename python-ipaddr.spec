%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           python-ipaddr
Version:        2.1.9
Release:        5%{?dist}
Summary:        A python library for working with IP addresses, both IPv4 and IPv6

Group:          Development/Languages
License:        ASL 2.0
URL:            http://code.google.com/p/ipaddr-py/
Source0:        http://ipaddr-py.googlecode.com/files/ipaddr-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel

%description
python-ipaddr is a library for working with IP addresses, both IPv4 and IPv6.
It was developed by Google for internal use, and is now open source.

%prep
%setup -q -n ipaddr-%{version}
# remove unneeded shebang
sed -i 1d ipaddr.py

%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING README RELEASENOTES
%{python_sitelib}/*


%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.1.9-5
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 23 2011 L.S. Keijser <keijser@stone-it.com> - 2.1.9-1
- new version from upstream

* Fri Feb 11 2011 L.S. Keijser <keijser@stone-it.com> - 2.1.8-1
- new version from upstream

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 14 2011 L.S. Keijser <keijser@stone-it.com> - 2.1.7-1
- new version from upstream

* Tue Sep 14 2010 L.S. Keijser <keijser@stone-it.com> - 2.1.5-1
- new version from upstream (included releasenotes again)

* Sat Aug 21 2010 L.S. Keijser <keijser@stone-it.com> - 2.1.4-2
- upstream didn't include RELEASENOTES file

* Tue Aug 17 2010 L.S. Keijser <keijser@stone-it.com> - 2.1.4-1
- new version from upstream

* Fri Jul 30 2010 L.S. Keijser <keijser@stone-it.com> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jun 15 2010 L.S. Keijser <keijser@stone-it.com> - 2.1.3-1
- new version from upstream
- added releasenotes file

* Tue Jun 01 2010 L.S. Keijser <keijser@stone-it.com> - 2.1.2-1
- new version from upstream

* Thu May 06 2010 L.S. Keijser <keijser@stone-it.com> - 2.1.1-1
- initial release

