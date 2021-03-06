%define		_status		beta
%define		_pearname	Services_Twitter
Summary:	%{_pearname} - PHP interface to Twitter's API
Summary(pl.UTF-8):	%{_pearname} - interfejs PHP do API serwisu Twitter
Name:		php-pear-%{_pearname}
Version:	0.7.0
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fa3a95dda3c4143360c92e5ac4cd9a66
URL:		http://pear.php.net/package/Services_Twitter/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.571
Requires:	php(json)
Requires:	php(mbstring)
Requires:	php(simplexml)
Requires:	php-pear
Requires:	php-pear-HTTP_Request2
Requires:	php-pear-PEAR-core >= 1:1.4.0
Suggests:	php-pear-HTTP_OAuth
Obsoletes:	php-pear-Services_Twitter-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(HTTP/OAuth.*)

%description
An interface for communicating with Twitter's public API. Send status
updates, fetch information, add friends, etc.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Interfejs umożliwiający komunikację z publicznym API serwisu Twitter.
Pozwala na wysyłanie aktualizacji statusów, pobieranie informacji,
dodawanie znajomych, itp.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/Twitter.php
%{php_pear_dir}/Services/Twitter

%{php_pear_dir}/data/%{_pearname}
