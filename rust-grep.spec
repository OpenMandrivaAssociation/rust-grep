# Generated by rust2rpm 9
%bcond_without check
%global debug_package %{nil}

%global crate grep

Name:           rust-%{crate}
Version:        0.2.4
Release:        5%{?dist}
Summary:        Fast line oriented regex searching as a library

# Upstream license specification: Unlicense/MIT
License:        Unlicense or MIT
URL:            https://crates.io/crates/grep
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Fast line oriented regex searching as a library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license COPYING UNLICENSE LICENSE-MIT
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+avx-accel-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+avx-accel-devel %{_description}

This package contains library source intended for building other packages
which use "avx-accel" feature of "%{crate}" crate.

%files       -n %{name}+avx-accel-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+grep-pcre2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+grep-pcre2-devel %{_description}

This package contains library source intended for building other packages
which use "grep-pcre2" feature of "%{crate}" crate.

%files       -n %{name}+grep-pcre2-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+pcre2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pcre2-devel %{_description}

This package contains library source intended for building other packages
which use "pcre2" feature of "%{crate}" crate.

%files       -n %{name}+pcre2-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+simd-accel-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+simd-accel-devel %{_description}

This package contains library source intended for building other packages
which use "simd-accel" feature of "%{crate}" crate.

%files       -n %{name}+simd-accel-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 12 13:01:11 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.4-3
- Dynamic BuildRequires

* Sun Jun 09 09:56:28 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.4-2
- Regenerate

* Tue Apr 16 13:39:47 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.4-1
- Update to 0.2.4

* Sun Mar 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.3-5
- Do not pull optional dependencies

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.3-3
- Rebuild

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.3-2
- Run tests in infrastructure

* Sun Sep 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3

* Sat Sep 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2

* Sat Aug 04 2018 Josh Stone <jistone@redhat.com> - 0.1.9-1
- Update to 0.1.9

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.8-3
- Bump regex to 1

* Wed Mar 14 2018 Josh Stone <jistone@redhat.com> - 0.1.8-2
- bump regex and regex-syntax

* Mon Feb 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.8-1
- Update to 0.1.8

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.7-2
- Rebuild for rust-packaging v5

* Wed Nov 08 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.7-1
- Update to 0.1.7

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.6-2
- Port to use rust-packaging

* Wed Mar 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.6-1
- Update to 0.1.6

* Sat Feb 25 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.5-1
- Initial package
