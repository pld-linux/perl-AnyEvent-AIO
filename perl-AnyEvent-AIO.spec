#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	AnyEvent
%define		pnam	AIO
Summary:	AnyEvent::AIO - truly asynchronous file and directory I/O
Summary(pl.UTF-8):	AnyEvent::AIO - w pełni asynchroniczne operacje we/wy dla plików i katalogów
Name:		perl-AnyEvent-AIO
Version:	1.1
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/ML/MLEHMANN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	faf3a4fe3dcffb04d27fbbd2c08651b9
URL:		http://search.cpan.org/dist/AnyEvent-AIO/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-AnyEvent >= 3.4
BuildRequires:	perl-IO-AIO >= 3.0
%endif
Requires:	perl-AnyEvent >= 3.4
Requires:	perl-IO-AIO >= 3.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AnyEvent::AIO is a module for truly asynchronous file and directory
I/O.

%description -l pl.UTF-8
AnyEvent::AIO to moduł udostępniający w pełni asynchroniczne operacje
we/wy dla plików i katalogów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/AnyEvent/AIO.pm
%{_mandir}/man3/AnyEvent::AIO.3pm*
