%global appid io.github.catpieleaf.Stud

%global debug_package %{nil}

%global __brp_strip %{nil}
%global __brp_strip_comment_note %{nil}
%global __brp_strip_static_archive %{nil}

%global __requires_exclude_from ^%{_prefix}/lib/stud/android-bionic/.*|^%{_libexecdir}/stud/lib64/.*|^%{_libexecdir}/stud/stud-runtime-bionic$
%global __provides_exclude_from ^%{_prefix}/lib/stud/(angle|android-bionic)/.*|^%{_libexecdir}/stud/lib64/.*

Name:           stud
Version:        1.1.2
Release:        1%{?dist}
Summary:        An Unofficial Open-Source Roblox Launcher for Linux

License:        AGPL-3.0-or-later
URL:            https://github.com/CatPieLeaf/Stud
Source0:        %{url}/releases/download/%{version}/stud-%{version}-x86_64.tar.zst
Packager:       CatPieLeaf <catpieleaf@proton.me>

ExclusiveArch:  x86_64

BuildRequires:  anda-srpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  zstd

Requires:       bubblewrap
Requires:       portaudio
Requires:       hicolor-icon-theme

Provides:       bundled(angle)
Provides:       bundled(swiftshader)
Provides:       bundled(vulkan-loader)
Provides:       bundled(fidelityfx-fsr1)

%description
Stud runs the real, unmodified Roblox app on your Linux desktop, in its own
window, with your mouse and keyboard. No browser, no emulator, no virtual
machine.

Links from a browser open straight into the experience, and the mouse and
keyboard behave the way they do in the desktop client. The game can render
below your screen's resolution and still fill it. Discord Rich
Presence carries a button friends can join through, and a tray menu names
the country a server is in when you join one.

Roblox is not included. You supply the Android application package yourself,
and Roblox remains subject to its own terms. Stud is an independent project,
not affiliated with, endorsed by or approved by Roblox Corporation.

%prep
%autosetup -c -n %{name}-%{version}

%build
# Deliberately empty: this package installs the release archive, which CI
# already built from the tag. ANGLE's own build fetches its dependencies
# as it runs, and the bionic set is extracted from an Android system
# image rather than compiled, so there is nothing to build here.

%install
cp -a usr %{buildroot}/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appid}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{appid}.metainfo.xml

%files
%license %{_datadir}/licenses/%{name}/LICENSE
%license %{_datadir}/licenses/%{name}/LICENSE.exception
%license %{_datadir}/licenses/%{name}/NOTICE.md
%license %{_datadir}/licenses/%{name}/android-bionic/
%license %{_datadir}/licenses/%{name}/angle/
%license %{_datadir}/licenses/%{name}/fidelityfx-fsr1/
%doc %{_datadir}/doc/%{name}/README.md
%doc %{_datadir}/doc/%{name}/copyright
%{_bindir}/%{name}
%{_prefix}/lib/%{name}/
%{_libexecdir}/%{name}/
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}.png
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Sep 15 2026 CatPieLeaf <catpieleaf@proton.me> - 1.1.2-1
- Update to 1.1.2

* Tue Sep 15 2026 CatPieLeaf <catpieleaf@proton.me> - 1.1.1-1
- Initial package
