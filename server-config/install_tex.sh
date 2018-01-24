#!/usr/bin/bash

# An error exit function
function error_exit
{
    echo "$1" 1>&2
    exit 1
}

# Download and unpack the latest TeX Live tarball
wget -q http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz || error_exit "Failure getting texlive tarball"
tar -xzf install-tl-unx.tar.gz || error_exit "Failure unpacking texlive tarball"
rm -f install-tl-unx.tar.gz

# Install with the small scheme
cd install-tl-20* || error_exit "Failure changing to texlive install directory"
echo 'selected_scheme scheme-small' > temp.profile
./install-tl -profile temp.profile || error_exit "Failure installing texlive core"
rm -f temp.profile

# Add the bin directory to the path
echo 'export PATH=/usr/local/texlive/2016/bin/x86_64-linux:$PATH' >> ~/.bashrc
source ~/.bashrc

# Install additional packages
tlmgr install latexmk || error_exit "Failure installing latexmk"
tlmgr install fncychap || error_exit "Failure installing fncychap"
tlmgr install titlesec || error_exit "Failure installing titlesec"
tlmgr install tabulary || error_exit "Failure installing tabulary"
tlmgr install varwidth || error_exit "Failure installing varwidth"
tlmgr install framed || error_exit "Failure installing framed"
tlmgr install wrapfig || error_exit "Failure installing wrapfig"
tlmgr install capt-of || error_exit "Failure installing capt-of"
tlmgr install helvetic || error_exit "Failure installing helvetic"
tlmgr install textpos || error_exit "Failure installing textpos"
tlmgr install hanging || error_exit "Failure installing hanging"
tlmgr install ulem || error_exit "Failure installing ulem"
tlmgr install needspace || error_exit "Failure installing needspace"
tlmgr install ec || error_exit "Failure installing ec"