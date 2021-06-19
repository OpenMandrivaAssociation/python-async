%define upstream_name async
%define debug_package %{nil}

Name: 		python-%{upstream_name}
Version: 	0.6.2
Release: 	1
Summary: 	Async Framework
License:	BSD
Group: 		Development/Python
Url: 		http://pypi.python.org/pypi/async
Source0: 	http://pypi.python.org/packages/source/a/async/async-%{version}.tar.gz
BuildRequires:  python-distribute

%description
Async is a framework to process interdependent tasks in a pool of workers.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc AUTHORS
%{python3_sitelib}/async
%{python3_sitelib}/async-%{version}-py%{py_ver}.egg-info
