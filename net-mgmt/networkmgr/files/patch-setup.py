--- setup.py.orig	2024-04-03 05:35:07 UTC
+++ setup.py
@@ -40,10 +40,7 @@ data_files = [
     (f'{prefix}/etc/sudoers.d', ['src/sudoers.d/networkmgr'])
 ]
 
-if os.path.exists('/etc/devd'):
-    data_files.append((f'{prefix}/etc/devd', ['src/networkmgr.conf']))
-if os.path.exists('/etc/devd-openrc'):
-    data_files.append((f'{prefix}/etc/devd-openrc', ['src/networkmgr.conf']))
+data_files.append((f'{prefix}/etc/devd', ['src/networkmgr.conf']))
 
 data_files.extend(datafilelist(f'{prefix}/share/icons/hicolor', 'src/icons'))
 
