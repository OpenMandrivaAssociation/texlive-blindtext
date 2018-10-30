# revision 25039
# category Package
# catalog-ctan /macros/latex/contrib/blindtext
# catalog-date 2011-11-23 08:28:31 +0100
# catalog-license lppl
# catalog-version 1.9c
Name:		texlive-blindtext
Version:	2.0
Release:	2
Summary:	Producing 'blind' text for testing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/blindtext
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/blindtext.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/blindtext.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/blindtext.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the commands \blindtext and \Blindtext for
creating 'blind' text useful in testing new classes and
packages, and \blinddocument, \Blinddocument for creating an
entire random document with sections, lists, mathematics, etc.
The package supports three languages, english, (n)german and
latin; the latin option provides a short "lorem ipsum" (for a
fuller lorem ipsum text, see the lipsum package).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/blindtext/blindtext.sty
%doc %{_texmfdistdir}/doc/latex/blindtext/README
%doc %{_texmfdistdir}/doc/latex/blindtext/blindtext.pdf
#- source
%doc %{_texmfdistdir}/source/latex/blindtext/blindtext.dtx
%doc %{_texmfdistdir}/source/latex/blindtext/blindtext.ins
%doc %{_texmfdistdir}/source/latex/blindtext/blindtext_american.dtx
%doc %{_texmfdistdir}/source/latex/blindtext/blindtext_catalan.dtx
%doc %{_texmfdistdir}/source/latex/blindtext/blindtext_english.dtx
%doc %{_texmfdistdir}/source/latex/blindtext/blindtext_french.dtx
%doc %{_texmfdistdir}/source/latex/blindtext/blindtext_german.dtx
%doc %{_texmfdistdir}/source/latex/blindtext/blindtext_latin.dtx
%doc %{_texmfdistdir}/source/latex/blindtext/blindtext_ngerman.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.9c-3
+ Revision: 758833
- texlive-blindtext

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.9c-2
+ Revision: 749767
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.9c-1
+ Revision: 717952
- texlive-blindtext
- texlive-blindtext
- texlive-blindtext
- texlive-blindtext
- texlive-blindtext

