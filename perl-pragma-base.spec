%define upstream_name    base
%define upstream_version 2.18
Name:		perl-pragma-%{upstream_name}
Version:	%perl_convert_version 2.18
Release:	3

Summary:	Compile-time class fields
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/fields/RGARCIA/base-2.18.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

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

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 2.150.0-2mdv2011.0
+ Revision: 656992
- rebuild for updated spec-helper

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 2.150.0-1mdv2011.0
+ Revision: 597199
- update to 2.15

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 2.140.0-2mdv2011.0
+ Revision: 552183
- rebuild

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 2.140.0-1mdv2010.0
+ Revision: 395228
- import perl-pragma-base


* Sun Jul 12 2009 cpan2dist 2.14-1mdv
- initial mdv release, generated with cpan2dist

