Name:		texlive-blindtext
Version:	1.9c
Release:	1
Summary:	Producing 'blind' text for testing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/blindtext
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/blindtext.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/blindtext.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/blindtext.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides the commands \blindtext and \Blindtext for
creating 'blind' text useful in testing new classes and
packages, and \blinddocument, \Blinddocument for creating an
entire random document with sections, lists, mathematics, etc.
The package supports three languages, english, (n)german and
latin; the latin option provides a short "lorem ipsum" (for a
fuller lorem ipsum text, see the lipsum package).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/blindtext/blindtext.sty
%doc %{_texmfdistdir}/doc/latex/blindtext/README
%doc %{_texmfdistdir}/doc/latex/blindtext/blindtext.pdf
#- source
%doc %{_texmfdistdir}/source/latex/blindtext/blindtext.dtx
%doc %{_texmfdistdir}/source/latex/blindtext/blindtext.ins
%doc %{_texmfdistdir}/source/latex/blindtext/blindtext_texts.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
