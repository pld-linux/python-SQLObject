
%define	module	SQLObject
%define _module sqlobject

Summary:	Object-Relational Manager, aka database wrapper
Name:		python-%{module}
Version:	0.6
Release:	1
License:	LGPL
Vendor:		Ian Bicking <ianb@colorstudy.com>
Group:		Development/Languages/Python
Source0:	http://prdownloads.sourceforge.net/sqlobject/%{module}-%{version}.tar.gz
# Source0-md5:	30867c7ca545653831b5de7d87632f19
URL:		http://sqlobject.org
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes created using SQLObject wrap database rows, presenting a
friendly-looking Python object instead of a database/SQL interface.
Emphasizes convenience.  Works with MySQL, Postgres, SQLite, Firebird.

%prep
%setup -q -n %{module}-%{version}

%build
env CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python -- setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt PKG-INFO docs examples
%{py_sitescriptdir}/%{_module}
