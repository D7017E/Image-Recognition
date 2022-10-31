# Setup GPU cluster

## Local Install Linux
A full guide if setup can be found [here](https://blog.ltu-ai.dev/python-setup-for-kubernetes-using-linux-gpu-enabled/).

TODO

## Local Install Windows
A full guide if setup can be found [here](https://blog.ltu-ai.dev/python-setup-for-kubernetes-using-windows/).

### 1. Requirement and Installation of Docker Desktop.

Start with checking your windows version and the windows version required by Docker Desktop: **Press Windows key + R: type “winver”**

Your Windows machine must meet the following requirements to successfully install Docker Desktop: **Install WSL 2 backend**

***WSL 2 backend requirements***

- Windows 11 64-bit: Home or Pro version 21H2 or higher, or Enterprise or Education version 21H2 or higher.

- Windows 10 64-bit: Home or Pro 2004 (build 19041) or higher, or Enterprise or Education 1909 (build 18363) or higher.

- Enable the WSL 2 feature on Windows. For detailed instructions, refer to the [Microsoft documentation](https://learn.microsoft.com/en-us/windows/wsl/install). You can also follow this link to [enable WSL 2 feature](https://www.configserverfirewall.com/windows-10/windows-subsystem-for-linux-2/) which I find handier than Microsoft documentation.

- The following hardware prerequisites are required to successfully run WSL 2 on Windows 10 or Windows 11:
  - 64-bit processor with [Second Level Address Translation (SLAT)](https://en.wikipedia.org/wiki/Second_Level_Address_Translation)
  - 4GB system RAM
  - BIOS-level hardware virtualization support must be enabled in the BIOS settings. For more information, see [Virtualization](https://docs.docker.com/desktop/troubleshoot/overview/#virtualization-must-be-enabled).
- Download and install the [Linux kernel update package](https://learn.microsoft.com/sv-se/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package).

Now execute the following command in Powershell
> wsl --set-default-version 2

Visit the official Docker website and install the [Docker Desktop](https://www.docker.com/products/docker-desktop/) package based on your Windows version.

### 2. Enable Kubernetes.
After installing docker go to Docker settings and enable Kubernetes. Click on Apply and restart, which will install and Start a Kubernetes single-node cluster when starting Docker Desktop.

Run the following command in Powershell to check it is installed or not.
> kubectl

### 3. Helm on Windows.
"sumrak" is a example of a username for the following:

- [Download](https://github.com/helm/helm/releases) the zip file for helm: Windows amd64

- Download and extract the folder “windows-amd64” and place it C:\Users\sumrak\docker

- Set the environment variable:
  - Press Windows key + R: type “SystemPropertiesAdvanced.exe”

  - Click environment variables: Under System variables, select Path, and then select Edit.

  - Select the New button and then add the folder path “C:\Users\sumrak\docker\windows-amd64” where you copied the helm folder to and then press OK.

Go to PowerShell and verify that helm is setup.
> helm

### 4. Install Required Visual Studio Extensions
Install the following extensions in vscode: 
- Docker
- Kubernetes
- Remote - Container
- Remote - SSH 
- Remote – SSH: Editing Configuration Files
- WSL
- Remote Development
- YAML
- Pylance
- Python
- Jupyter
- Jupyter Keymap
- Jupyter Notebook Renderers

