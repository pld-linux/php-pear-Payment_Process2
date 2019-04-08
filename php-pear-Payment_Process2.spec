%include	/usr/lib/rpm/macros.php
%define		_class		Payment
%define		_subclass	Process2
%define		_status		alpha
%define		_pearname	Payment_Process2

Summary:	%{_pearname} - A PHP5 Payment process API
#Summary(pl.UTF-8):	%{_pearname} - 
Name:		php-pear-%{_pearname}
Version:	0.3.1
Release:	2
License:	BSD Style
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6dacc74ee670d5608509472ddf89af7e
Patch0:		%{name}-path.patch
URL:		http://pear.php.net/package/Payment_Process2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Obsoletes:	php-pear-Payment_Process2-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A PHP5 Payment process API using HTTP_Request2

In PEAR status of this package is: %{_status}.

#%description -l pl.UTF-8
#...
#
#Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/Payment_Process2/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Payment/Process2.php
%{php_pear_dir}/Payment/Process2
%{php_pear_dir}/data/Payment_Process2
