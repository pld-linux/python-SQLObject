
%define	module	SQLObject
%define _module sqlobject

Summary:	Object-Relational Manager, aka database wrapper
Summary(pl):	Zarz±dca obiektowo-relacyjny, czyli wrapper dla baz danych
Name:		python-%{module}
Version:	0.7.0
Release:	1
License:	LGPL
Vendor:		Ian Bicking <ianb@colorstudy.com>
Group:		Development/Languages/Python
Source0:	http://cheeseshop.python.org/packages/source/S/SQLObject/%{module}-%{version}.tar.gz
# Source0-md5:	dccb921b5df6a15312b56630ac4ac205
Patch0:		%{name}-disable-setuptools.patch
URL:		http://sqlobject.org
BuildRequires:	python-devel >= 1:2.3
%pyrequires_eq	python-modules
Requires:	python-FormEncode >= 0.2.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes created using SQLObject wrap database rows, presenting a
friendly-looking Python object instead of a database/SQL interface.
Emphasizes convenience. Works with MySQL, PostgreSQL, SQLite,
Firebird.

%description -l pl
Klasy tworzone przy u¿yciu SQLObject opakowuj± wiersze bazy danych,
prezentuj±c przyja¼nie wygl±daj±cy obiekt Pythona zamiast interfejsu
bazy danych/SQL. Nacisk po³o¿ony jest na wygodê. Dzia³a z MySQL-em,
PostgreSQL-em, SQLite, Firebirdem.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
rm -rf ez_setup
python setup.py build

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
%doc README.txt PKG-INFO docs 
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{_module}
