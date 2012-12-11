%define upstream_name async

Name: 		python-%{upstream_name}
Version: 	0.6.1
Release: 	2
Summary: 	Async Framework
License:	BSD
Group: 		Development/Python
Url: 		http://pypi.python.org/pypi/async
Source0: 	http://pypi.python.org/packages/source/a/async/async-%{version}.tar.gz
BuildRequires:  python-distribute

%description
Async is a framework to process interdependent tasks in a pool of workers.

%prep
%setup -q -n %upstream_name-%version

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc AUTHORS README
%{python_sitearch}/async
%{python_sitearch}/async-%{version}-py%{py_ver}.egg-info


%changelog
* Mon Jun 27 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.1-1mdv2011.0
+ Revision: 687479
- import python-async

