%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	Twitter
%define		_status		beta
%define		_pearname	Services_Twitter

Summary:	%{_pearname} - PHP interface to Twitter's API
Summary(pl.UTF-8):	%{_pearname} - interfejs PHP do API serwisu Twitter
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6d43a0d450157832614730c432e371c7
URL:		http://pear.php.net/package/Services_Twitter/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An interface for communicating with Twitter's public API. Send status
updates, fetch information, add friends, etc.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Interfejs umożliwiający komunikację z publicznym API serwisu Twitter.
Pozwala na wysyłanie aktualizacji statusów, pobieranie informacji,
dodawanie znajomych, itp.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/%{_subclass}.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Services_Twitter
