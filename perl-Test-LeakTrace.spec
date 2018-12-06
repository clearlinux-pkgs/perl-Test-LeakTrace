#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-LeakTrace
Version  : 0.16
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/L/LE/LEEJO/Test-LeakTrace-0.16.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/L/LE/LEEJO/Test-LeakTrace-0.16.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtest-leaktrace-perl/libtest-leaktrace-perl_0.16-1.debian.tar.xz
Summary  : 'Traces memory leaks'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-LeakTrace-lib = %{version}-%{release}
Requires: perl-Test-LeakTrace-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This is Perl module Test::LeakTrace.
INSTALLATION
Test::LeakTrace installation is straightforward. If your CPAN shell is set up,
you should just be able to do

%package dev
Summary: dev components for the perl-Test-LeakTrace package.
Group: Development
Requires: perl-Test-LeakTrace-lib = %{version}-%{release}
Provides: perl-Test-LeakTrace-devel = %{version}-%{release}

%description dev
dev components for the perl-Test-LeakTrace package.


%package lib
Summary: lib components for the perl-Test-LeakTrace package.
Group: Libraries
Requires: perl-Test-LeakTrace-license = %{version}-%{release}

%description lib
lib components for the perl-Test-LeakTrace package.


%package license
Summary: license components for the perl-Test-LeakTrace package.
Group: Default

%description license
license components for the perl-Test-LeakTrace package.


%prep
%setup -q -n Test-LeakTrace-0.16
cd ..
%setup -q -T -D -n Test-LeakTrace-0.16 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Test-LeakTrace-0.16/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-LeakTrace
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Test-LeakTrace/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Test/LeakTrace.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Test/LeakTrace/JA.pod
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Test/LeakTrace/Script.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::LeakTrace.3
/usr/share/man/man3/Test::LeakTrace::JA.3
/usr/share/man/man3/Test::LeakTrace::Script.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/Test/LeakTrace/LeakTrace.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-LeakTrace/deblicense_copyright
