Name:           virtual-keyboard
Version:        1.0
Release:        1%{?dist}
Summary:        Virtual keyboard with key press visualization

License:        MIT
URL:            https://github.com/BajiKeiske/Key-Listener
Source0:        %{name}-%{version}.tar.gz

%define _noautoreq 1
Requires: python3

%description
Virtual keyboard application that shows pressed keys with visual feedback.
Includes physical key press detection and on-screen keyboard visualization.

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datarootdir}/applications

# Install Python files
cp -r *.py %{buildroot}%{_datadir}/%{name}/

# Create launcher script
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/sh
exec python3 %{_datadir}/%{name}/main.py
EOF
chmod 755 %{buildroot}%{_bindir}/%{name}

# Create desktop file
cat > %{buildroot}%{_datarootdir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Virtual Keyboard
Comment=Keyboard key press visualizer
Exec=%{_bindir}/%{name}
Icon=keyboard
Terminal=false
Type=Application
Categories=Utility;
EOF

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datarootdir}/applications/%{name}.desktop

%changelog
* Sun Jul 13 2025 BajiKeiske <kus163166@gmail.com> - 1.0-1
- Initial package
