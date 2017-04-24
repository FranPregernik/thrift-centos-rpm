Name:             thrift
Version:          0.9.3
Release:          1%{?dist}
Summary:          A multi-language RPC and serialization framework

Group:            System Environment/Libraries
License:          ASL 2.0
URL:              http://incubator.apache.org/thrift
Source0:          https://archive.apache.org/dist/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:    byacc
BuildRequires:    boost-devel >= 1.33.1
BuildRequires:    dos2unix
BuildRequires:    flex
BuildRequires:    libevent-devel
BuildRequires:    libtool
BuildRequires:    mono-devel >= 1.2.6
BuildRequires:    zlib-devel

%description
Thrift is a software framework for scalable cross-language services
development. It combines a powerful software stack with a code generation
engine to build services that work efficiently and seamlessly between C++,
Java, C#, Python, Ruby, Perl, PHP, Objective C/Cocoa, Smalltalk, Erlang,
Objective Caml, and Haskell.

%prep
%setup -q
#%patch0 -p1

# Fix spurious-executable-perm warning
find tutorial/ -type f -exec chmod 0644 {} \;

# Haskell setup script won't run with blank or comment lines
sed -i '/#/d;/^$/d' lib/hs/Setup.lhs

%build
%configure \
  --without-c \
  --without-cpp \
  --without-c_glib \
  --without-haskell \
  --without-java \
  --without-perl \
  --without-php \
  --without-python \
  --without-ruby \
  --without-erlang \
  --enable-static=yes
%{__make}

%install
%{__rm} -rf %{buildroot}

# Install everything not listed below
%{__make} DESTDIR=%{buildroot} install
# Remove "la" files
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

# Fix non-standard-executable-perm

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/thrift

%changelog
* Thu Dec 26 2013 Aldrin Leal - 0.9.1-1
- Hack for 0.9.1 on CentOS

* Thu May 16 2013 Brian Cline <brian.cline@gmail.com> - 0.9.0-1
- Update to 0.9.0

* Tue Nov 02 2010 Silas Sewell <silas@sewell.ch> - 0.5.0-1
- Update to 0.5.0

* Mon Mar 01 2010 Silas Sewell <silas@sewell.ch> - 0.2.0-1
- Update to non-snapshot release
- Various tweaks for release package
- Add flag for csharp build

* Thu Jan 07 2010 Silas Sewell <silas@sewell.ch> - 0.2-0.6.20091112svn835538
- Disable ghc until rawhide is fixed

* Thu Jan 07 2010 Silas Sewell <silas@sewell.ch> - 0.2-0.5.20091112svn835538
- Add ghc-network-prof and ghc-network-devel dependencies

* Tue Dec 08 2009 Silas Sewell <silas@sewell.ch> - 0.2-0.4.20091112svn835538
- Tweaks for EL compatibility

* Thu Nov 12 2009 Silas Sewell <silas@sewell.ch> - 0.2-0.3.20091112svn835538
- Update to latest snapshot

* Mon Jul 20 2009 Silas Sewell <silas@sewell.ch> - 0.2-0.2.20090720svn795861
- Update to latest snapshot

* Mon May 25 2009 Silas Sewell <silas@sewell.ch> - 0.2-0.1.20090525svn777690
- Update to latest snapshot
- Fix version, release syntax and perl requires

* Wed May 06 2009 Silas Sewell <silas@sewell.ch> - 0.0-0.1.20090505svn770888
- Fix various require issues
- Change lib to cpp and devel to cpp-devel
- Use ghc version macro
- Add documentation to language specific libraries

* Fri May 01 2009 Silas Sewell <silas@sewell.ch> - 0.0-0.0.20090501svn770888
- Initial build
