%run -i 'load_notebook_finder.py'
sys.meta_path.append(NotebookFinder())

import MCIBase
dir(MCIBase) 