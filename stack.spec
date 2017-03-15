# nothing to see here
%global debug_package %{nil}

%bcond_with tests

Name:           stack
Version:        1.4.0
Release:        1%{?dist}
Summary:        The Haskell Stack Tool

License:        BSD
Url:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
#BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-aeson-devel
#BuildRequires:  ghc-annotated-wl-pprint-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base-compat-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-binary-devel
#BuildRequires:  ghc-binary-tagged-devel
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-bytestring-devel
#BuildRequires:  ghc-clock-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-extra-devel
BuildRequires:  ghc-containers-devel
#BuildRequires:  ghc-cryptonite-conduit-devel
#BuildRequires:  ghc-cryptonite-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
#BuildRequires:  ghc-either-devel
#BuildRequires:  ghc-errors-devel
BuildRequires:  ghc-exceptions-devel
#BuildRequires:  ghc-extra-devel
#BuildRequires:  ghc-fast-logger-devel
#BuildRequires:  ghc-file-embed-devel
#BuildRequires:  ghc-filelock-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-fsnotify-devel
#BuildRequires:  ghc-generic-deriving-devel
#BuildRequires:  ghc-gitrev-devel
#BuildRequires:  ghc-hackage-security-devel
BuildRequires:  ghc-hashable-devel
#BuildRequires:  ghc-hastache-devel
#BuildRequires:  ghc-hit-devel
#BuildRequires:  ghc-hpack-devel
BuildRequires:  ghc-hpc-devel
#BuildRequires:  ghc-http-client-devel
#BuildRequires:  ghc-http-client-tls-devel
#BuildRequires:  ghc-http-conduit-devel
BuildRequires:  ghc-http-types-devel
#BuildRequires:  ghc-lifted-async-devel
BuildRequires:  ghc-lifted-base-devel
#BuildRequires:  ghc-memory-devel
#BuildRequires:  ghc-microlens-devel
#BuildRequires:  ghc-microlens-mtl-devel
BuildRequires:  ghc-monad-control-devel
#BuildRequires:  ghc-monad-logger-devel
#BuildRequires:  ghc-monad-unlift-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-uri-devel
#BuildRequires:  ghc-open-browser-devel
BuildRequires:  ghc-optparse-applicative-devel
#BuildRequires:  ghc-optparse-simple-devel
#BuildRequires:  ghc-path-devel
#BuildRequires:  ghc-path-io-devel
#BuildRequires:  ghc-persistent-devel
#BuildRequires:  ghc-persistent-sqlite-devel
#BuildRequires:  ghc-persistent-template-devel
#BuildRequires:  ghc-pid1-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-process-devel
#BuildRequires:  ghc-project-template-devel
#BuildRequires:  ghc-regex-applicative-text-devel
BuildRequires:  ghc-resourcet-devel
#BuildRequires:  ghc-retry-devel
BuildRequires:  ghc-safe-devel
#BuildRequires:  ghc-safe-exceptions-devel
BuildRequires:  ghc-semigroups-devel
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-stm-devel
#BuildRequires:  ghc-store-devel
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-tar-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-temporary-devel
#BuildRequires:  ghc-text-binary-devel
BuildRequires:  ghc-text-devel
#BuildRequires:  ghc-text-metrics-devel
BuildRequires:  ghc-time-devel
#BuildRequires:  ghc-tls-devel
BuildRequires:  ghc-transformers-base-devel
BuildRequires:  ghc-transformers-devel
#BuildRequires:  ghc-unicode-transforms-devel
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-binary-instances-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-yaml-devel
BuildRequires:  ghc-zip-archive-devel
BuildRequires:  ghc-zlib-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-mono-traversable-devel
BuildRequires:  ghc-neat-interpolation-devel
BuildRequires:  ghc-smallcheck-devel
BuildRequires:  ghc-th-reify-many-devel
%endif
# End cabal-rpm deps
ExclusiveArch:  %{ghc_arches_with_ghci}
# for ignore -> pcre-heavy
%if 0%{?nofedora} >= 22
BuildRequires:  ghc-pcre-light-devel
%else
BuildRequires:  pcre-devel
BuildRequires:  zlib-devel
%endif
BuildRequires:  cabal-install > 1.18

# for upstream binary ghc tarballs linked to libtinfo.so.5
%if 0%{?nofedora} >= 24
Requires:       ncurses-compat-libs
%endif

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
%doc LICENSE .cabal-sandbox/share/doc/*/*
%doc README.md
%{_bindir}/%{name}


%changelog
* Wed Mar 15 2017 Jens Petersen <petersen@redhat.com> - 1.4.0-1
- update to 1.4.0
- https://docs.haskellstack.org/en/stable/ChangeLog/#140

* Wed Dec 28 2016 Jens Petersen <petersen@redhat.com> - 1.3.2-1
- update to 1.3.2

* Fri Dec 16 2016 Jens Petersen <petersen@redhat.com> - 1.3.0-1
- 1.3.0 release
- https://github.com/commercialhaskell/stack/releases/tag/v1.3.0

* Thu Sep 22 2016 Jens Petersen <petersen@redhat.com> - 1.2.0-1

* Sat May 21 2016 Jens Petersen <petersen@fedoraproject.org> - 1.1.2-1

* Thu May  5 2016 Jens Petersen <petersen@redhat.com> - 1.1.0-1
- update to 1.1.0

* Mon Apr 11 2016 Jens Petersen <petersen@redhat.com> - 1.0.4.3-1
- update to 1.0.4.3

* Mon Apr  4 2016 Jens Petersen <petersen@redhat.com> - 1.0.4.2-2
- require ncurses-compat-libs for F24+ to help people use upstream ghc tarballs
  (thanks Jan Synacek)

* Thu Mar 10 2016 Jens Petersen <petersen@redhat.com> - 1.0.4.2-1
- update to 1.0.4.2

* Fri Feb 26 2016 Jens Petersen <petersen@redhat.com> - 1.0.4.1-1
- update to 1.0.4.1

* Tue Jan 19 2016 Jens Petersen <petersen@redhat.com> - 1.0.2-1
- update to 1.0.2

* Fri Jan  8 2016 Jens Petersen <petersen@redhat.com> - 1.0.0-1
- update to 1.0.0

* Fri Dec 18 2015 Jens Petersen <petersen@redhat.com> - 0.1.10.1-1
- update to 0.1.10.1

* Wed Dec  9 2015 Jens Petersen <petersen@redhat.com> - 0.1.10.0-1
- update to 0.1.10.0
- build with ghc-7.10 and assume only ghc libs

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
