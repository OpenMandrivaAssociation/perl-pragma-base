%define upstream_name    base
Name:		perl-pragma-%{upstream_name}
Version:	2.23
Release:	1

Summary:	Compile-time class fields
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/base
Source0:	https://cpan.metacpan.org/authors/id/R/RJ/RJBS/base-2.23.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildArch:	noarch
Provides:	perl(base)

%description
Unless you are using the 'fields' pragma, consider this module discouraged
in favor of the lighter-weight 'parent'.

Allows you to both load one or more modules, while setting up inheritance
from those modules at the same time. Roughly similar in effect to

    package Baz;
    BEGIN {
        require Foo;
        require Bar;
        push @ISA, qw(Foo Bar);
    }

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

