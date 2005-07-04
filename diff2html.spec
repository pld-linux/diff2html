Summary:	diff2html - utility generates an HTML page to display the output of the diff
Summary(fr):	L'utilitaire diff2html génère une page HTML valide pour afficher le résultat de l'utilitaire bien connu diff
Summary(pl):	diff2html - narzêdzie generuj±ce stronê HTML wy¶wietlaj±c± wyj¶cie narzêdzia diff
Name:		diff2html
Version:	1.0.1
Release:	0.1
License:	GPL
Group:		Applications/Text
Source0:	http://kafka.fr.free.fr/diff2html/diff2html.bz2
# Source0-md5:	e3aa3bd4fec0a93f5f97efcd210e232b
URL:		http://kafka.fr.free.fr/diff2html/
Requires:	python
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The diff2html utility generates an HTML page to display the output of
the diff(1) well-known utility. Using Cascading Style Sheets, the user
can fully personalize the appearance of the web page (you might find
the default styles are too much colorful).

%description -l fr
L'utilitaire diff2html génère une page HTML valide pour afficher le
résultat de l'utilitaire bien connu diff. Par l'utilisation des
feuilles de styles CSS2, l'utilisateur peut complètement personnaliser
l'apparence de la page web (vous pouvez estimer que les styles par
défaut sont trop colorés). diff2html est écrit en langage Python et
est soumis à la license GNU GPL.

%description -l pl
narzêdzie diff2html generuje stronê HTML wy¶wietlaj±c± wyj¶cie innego
dobrze znanego narzêdzia diff. U¿ywaj±c kaskadowych stylów (CSS) mo¿na
w pe³ni spersonalizowaæ wygl±d strony.

%prep
%setup -q -c -T
install %{SOURCE0} .
bunzip2 %{name}.bz2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
