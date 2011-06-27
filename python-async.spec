%define upstream_name async
%define name    python-%{upstream_name}
%define version 0.6.1
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Async Framework
License:	BSD
Group: 		Development/Python
Url: 		http://pypi.python.org/pypi/async
Source0: 	http://pypi.python.org/packages/source/a/async/async-%{version}.tar.gz
BuildRequires:  python-distribute
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Async is a framework to process interdependent tasks in a pool of workers.

%prep
%setup -q -n %upstream_name-%version

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README
%{python_sitearch}/async
%{python_sitearch}/async-%{version}-py%{pyver}.egg-info
