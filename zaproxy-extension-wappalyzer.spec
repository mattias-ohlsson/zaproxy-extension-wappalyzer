Name:           zaproxy-extension-wappalyzer
Version:        
Release:        1%{?dist}
Summary:        

License:        
URL:            
Source0:        

BuildRequires:  
Requires:       

%description


%prep
%autosetup


%build
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license add-license-file-here
%doc add-docs-here



%changelog
* Mon Feb 24 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com>
- 
