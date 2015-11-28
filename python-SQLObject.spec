
%define	module	SQLObject
%define _module sqlobject

Summary:	Object-Relational Manager, aka database wrapper
Summary(pl.UTF-8):	Zarządca obiektowo-relacyjny, czyli wrapper dla baz danych
Name:		python-%{module}
Version:	0.10.4
Release:	3
License:	LGPL
Vendor:		Ian Bicking <ianb@colorstudy.com>
Group:		Development/Languages/Python
Source0:	http://cheeseshop.python.org/packages/source/S/SQLObject/%{module}-%{version}.tar.gz
# Source0-md5:	20039279c5b799c49e6496b9fe71f03f
URL:		http://sqlobject.org
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-FormEncode >= 0.2.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes created using SQLObject wrap database rows, presenting a
friendly-looking Python object instead of a database/SQL interface.
Emphasizes convenience. Works with MySQL, PostgreSQL, SQLite,
Firebird.

%description -l pl.UTF-8
Klasy tworzone przy użyciu SQLObject opakowują wiersze bazy danych,
prezentując przyjaźnie wyglądający obiekt Pythona zamiast interfejsu
bazy danych/SQL. Nacisk położony jest na wygodę. Działa z MySQL-em,
PostgreSQL-em, SQLite, Firebirdem.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

python -- setup.py install \
	--single-version-externally-managed \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt PKG-INFO docs 
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{_module}
%{py_sitescriptdir}/SQLObject*
