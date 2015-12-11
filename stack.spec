# nothing to see here
%global debug_package %{nil}

%bcond_with tests

Name:           stack
Version:        0.1.10.0
Release:        1%{?dist}
Summary:        The Haskell Tool Stack

License:        BSD
Url:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        https://www.stackage.org/lts-3/cabal.config

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hpc-devel
#BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-process-devel
#BuildRequires:  ghc-semigroups-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
ExclusiveArch:  %{ghc_arches_with_ghci}
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-hspec-devel
%endif
# End cabal-rpm deps
# for ignore -> pcre-heavy
%if 0%{?nofedora} >= 22
BuildRequires:  ghc-pcre-light-devel
%else
BuildRequires:  pcre-devel
BuildRequires:  zlib-devel
%endif
BuildRequires:  cabal-install > 1.18

%description
Please see the README.md for usage information, and the wiki on Github for more
details. Also, note that the API for the library is not currently stable, and
may change significantly, even between minor releases. It is currently only
intended for use by the executable.


%prep
%setup -q
cp -p %{SOURCE1} .


%build
%global cabal cabal
[ -d "$HOME/.cabal" ] || %cabal update
%cabal sandbox init
%cabal install --force-reinstalls


%install
mkdir -p %{buildroot}%{_bindir}
install -p .cabal-sandbox/bin/%{name} %{buildroot}%{_bindir}


%check
%if %{with tests}
%cabal test
%endif


%files
%doc LICENSE .cabal-sandbox/share/doc/*/*
%doc README.md
%{_bindir}/%{name}


%changelog
* Wed Dec  9 2015 Jens Petersen <petersen@redhat.com> - 0.1.10.0-1
- update to 0.1.10.0
- build with ghc-7.10 and assume only ghc libs
- use lts-3 cabal.config

* Mon Nov 30 2015 Jens Petersen <petersen@redhat.com> - 0.1.8.0-1
- 0.1.8.0

* Thu Oct 22 2015 Jens Petersen <petersen@redhat.com> - 0.1.6.0-1
- update to 0.1.6.0

* Sat Oct  3 2015 Jens Petersen <petersen@fedoraproject.org> - 0.1.5.0-1
- 0.1.5.0

* Wed Sep 02 2015 Jens Petersen <petersen@redhat.com> - 0.1.3.1-1
- update to 0.1.3.1

* Mon Jul 13 2015 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.1.2.0-1
- spec file generated by cabal-rpm-0.9.6.50
