
%define	module	SQLObject
%define _module sqlobject

Summary:	Object-Relational Manager, aka database wrapper
Summary(pl):	Zarz±dca obiektowo-relacyjny, czyli wrapper dla baz danych
Name:		python-%{module}
Version:	0.6
Release:	1
License:	LGPL
Vendor:		Ian Bicking <ianb@colorstudy.com>
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/sqlobject/%{module}-%{version}.tar.gz
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
Emphasizes convenience. Works with MySQL, PostgreSQL, SQLite,
Firebird.

%description -l pl
Klasy tworzone przy u¿yciu SQLObject opakowuj± wiersze bazy danych,
prezentuj±c przyja¼nie wygl±daj±cy obiekt Pythona zamiast interfejsu
bazy danych/SQL. Nacisk po³o¿ony jest na wygodê. Dzia³a z MySQL-em,
PostgreSQL-em, SQLite, Firebirdem.

%prep
%setup -q -n %{module}-%{version}

%build
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
%doc README.txt PKG-INFO docs examples
%{py_sitescriptdir}/%{_module}
