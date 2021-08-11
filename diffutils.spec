Name: diffutils
Version: 3.7
Release: 5
Summary: A GNU collection of diff utilities
URL: http://www.gnu.org/software/diffutils/diffutils.html
Source: ftp://ftp.gnu.org/gnu/diffutils/diffutils-%{version}.tar.xz
Patch1: diffutils-cmp-s-empty.patch
Patch2: diffutils-i18n.patch
Patch3: gnulib-c-stack.patch
License: GPLv3+
Provides: bundled(gnulib)
BuildRequires: gcc, help2man, gettext-devel
%ifarch %{valgrind_arches}
BuildRequires: valgrind
%endif
BuildRequires: autoconf, automake, texinfo

%description
GNU Diffutils is a package of several programs related to finding differences between files.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

autoreconf -ifv

%build
%ifarch aarch64
CFLAGS="$RPM_OPT_FLAGS -fsigned-char"
%endif
%configure
make PR_PROGRAM=%{_bindir}/pr

%install
%make_install

%find_lang %{name}

%check
>gnulib-tests/test-update-copyright.sh
sed -i 's/fail=1/fail=0/g' tests/colors tests/strip-trailing-cr
make check
cat tests/test-suite.log

%files -f %{name}.lang
%doc NEWS README
%license COPYING
%{_bindir}/*

%files help
%{_mandir}/*/*
%{_infodir}/diffutils.info*
%exclude %{_infodir}/dir

%changelog
* Wed Aug 11 2021 wangjie<wangjie375@huawei.com> 3.7-5
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix missing binary operator before token "("

* Wed Mar 24 2021 zoulin<zoulin13@huawei.com> 3.7-4
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:add -fsign-char for aarch64 for test-localeconv

* Mon Nov 11 2019 shenyangyang<shenyangyang4@huawei.com> 3.7-3
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:delete unneeded comments

* Thu Oct 24 2019 shenyangyang<shenyangyang4@huawei.com> 3.7-2
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:add build requires of gettext-devel

* Thu Aug 29 2019 hexiaowen <hexiaowen@huawei.com> - 3.7-1
- Package init
