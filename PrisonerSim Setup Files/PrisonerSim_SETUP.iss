; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Prisoner Simulation"
#define MyAppVersion "1.2.0"
#define MyAppPublisher "The Yay Company"
#define MyAppURL "https://www.yaycompany.com"
#define MyAppExeName "PrisonerSim TLS.exe"
#define MyAppAssocName "PrisonerSim"
#define MyAppAssocExt ".exe"
#define MyAppAssocKey StringChange(MyAppAssocName, " ", "") + MyAppAssocExt

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{794F36E1-C90E-4878-98E6-B68C50D7F160}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\PrisonerSim
ChangesAssociations=yes
DisableProgramGroupPage=yes
; Remove the following line to run in administrative install mode (install for all users.)
PrivilegesRequired=lowest
OutputDir=D:\matty\Documents\Code\PrisonerSim TLS\PrisonerSim Setup Files
OutputBaseFilename=PrisonerSim_SETUP
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "D:\matty\Documents\Code\PrisonerSim TLS\bin\Release\net6.0\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\matty\Documents\Code\PrisonerSim TLS\bin\Release\net6.0\PrisonerSim TLS.deps.json"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\matty\Documents\Code\PrisonerSim TLS\bin\Release\net6.0\PrisonerSim TLS.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\matty\Documents\Code\PrisonerSim TLS\bin\Release\net6.0\PrisonerSim TLS.pdb"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\matty\Documents\Code\PrisonerSim TLS\bin\Release\net6.0\PrisonerSim TLS.runtimeconfig.json"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocExt}\OpenWithProgids"; ValueType: string; ValueName: "{#MyAppAssocKey}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}"; ValueType: string; ValueName: ""; ValueData: "{#MyAppAssocName}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppExeName},0"
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""
Root: HKA; Subkey: "Software\Classes\Applications\{#MyAppExeName}\SupportedTypes"; ValueType: string; ValueName: ".myp"; ValueData: ""

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
