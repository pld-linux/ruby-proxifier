%define	pkgname	proxifier
Summary:	Proxifier is a gem to force ruby to use a proxy
Name:		ruby-%{pkgname}
Version:	1.0.3
Release:	1
License:	BSD-like
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	abfb31d36a2ea4feac73cd2f0363feaa
URL:		https://github.com/samuelkadolph/ruby-proxifier
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proxifier adds support for HTTP or SOCKS proxies and lets you force
TCPSocket to use proxies.

%prep
%setup -q -n %{pkgname}-%{version}
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pirb
%attr(755,root,root) %{_bindir}/pruby
%{ruby_vendorlibdir}/proxifier.rb
%{ruby_vendorlibdir}/proxifier
%dir %{ruby_vendorlibdir}/uri
%{ruby_vendorlibdir}/uri/socks.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
