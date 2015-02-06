%define upstream_name    Number-Nary
%define upstream_version 1.100312

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Encode and decode numbers as n-ary strings
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Number/Number-Nary-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(UDCode)
BuildArch:	noarch

%description
no description found

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
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.100.311-2mdv2011.0
+ Revision: 654268
- rebuild for updated spec-helper

* Mon Feb 01 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.311-1mdv2011.0
+ Revision: 498981
- update to 1.100311

* Thu Dec 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.108.0-1mdv2010.1
+ Revision: 472801
- import perl-Number-Nary


* Thu Dec 03 2009 cpan2dist 0.108-1mdv
- initial mdv release, generated with cpan2dist

