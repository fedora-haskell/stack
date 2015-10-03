# nothing to see here
%global debug_package %{nil}

%bcond_with tests

Name:           stack
Version:        0.1.5.0
Release:        1%{?dist}
Summary:        The Haskell Tool Stack

License:        BSD
Url:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
#BuildRequires:  chrpath
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-base64-bytestring-devel
#BuildRequires:  ghc-bifunctors-devel
BuildRequires:  ghc-binary-devel
#BuildRequires:  ghc-binary-tagged-devel
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-byteable-devel
BuildRequires:  ghc-bytestring-devel
#BuildRequires:  ghc-conduit-combinators-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-extra-devel
BuildRequires:  ghc-containers-devel
#BuildRequires:  ghc-cryptohash-conduit-devel
BuildRequires:  ghc-cryptohash-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
#BuildRequires:  ghc-either-devel
#BuildRequires:  ghc-enclosed-exceptions-devel
BuildRequires:  ghc-exceptions-devel
#BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-fast-logger-devel
#BuildRequires:  ghc-file-embed-devel
#BuildRequires:  ghc-filelock-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-fsnotify-devel
#BuildRequires:  ghc-gitrev-devel
BuildRequires:  ghc-hashable-devel
#BuildRequires:  ghc-hastache-devel
#BuildRequires:  ghc-http-client-devel
#BuildRequires:  ghc-http-client-tls-devel
#BuildRequires:  ghc-http-conduit-devel
BuildRequires:  ghc-http-types-devel
#BuildRequires:  ghc-ignore-devel
BuildRequires:  ghc-lifted-base-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-monad-logger-devel
BuildRequires:  ghc-monad-loops-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-optparse-applicative-devel
#BuildRequires:  ghc-optparse-simple-devel
#BuildRequires:  ghc-path-devel
#BuildRequires:  ghc-persistent-devel
#BuildRequires:  ghc-persistent-sqlite-devel
#BuildRequires:  ghc-persistent-template-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-process-devel
#BuildRequires:  ghc-project-template-devel
BuildRequires:  ghc-resourcet-devel
#BuildRequires:  ghc-retry-devel
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-tar-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-base-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-binary-instances-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-void-devel
BuildRequires:  ghc-word8-devel
BuildRequires:  ghc-yaml-devel
BuildRequires:  ghc-zlib-devel
ExclusiveArch:  %{ghc_arches_with_ghci}
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-hspec-devel
%endif
# End cabal-rpm deps
# for ignore -> pcre-heavy
BuildRequires:  ghc-pcre-light-devel
BuildRequires:  cabal-install > 1.18

%description
Please see the README.md for usage information, and the wiki on Github for more
details. Also, note that the API for the library is not currently stable, and
may change significantly, even between minor releases. It is currently only
intended for use by the executable.


%prep
%setup -q


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
%license .cabal-sandbox/share/doc/*/*
%doc README.md
%{_bindir}/%{name}


%changelog
* Sat Oct  3 2015 Jens Petersen <petersen@fedoraproject.org> - 0.1.5.0-1
- 0.1.5.0

* Wed Sep 02 2015 Jens Petersen <petersen@redhat.com> - 0.1.3.1-1
- update to 0.1.3.1

* Mon Jul 13 2015 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.1.2.0-1
- spec file generated by cabal-rpm-0.9.6.50
