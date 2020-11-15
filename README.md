# Windows Lockscreen Puller

Grabs the lockscreen images from within windows.

## Use

1. Change the name of the user directory in `collect_config.py`.
2. Install pillow by running `pip install Pillow`.
3. Run the script `python collect.py` to remove to collect wallpapers.
4. Run the script `python remove_duplicate_images.py` to remove duplicate wallpapers.

## Next

1. It would be great if we could add variable to the path which makes python fill in the user directory.

2. Configure how Lockscreens are pulled with the `config.json` file. The default config looks like this:
```javascript
{
  // The path to collect the Lock Screen Wallpapers from
  assetsPath: "\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets",

  // The path where the desktop wallpapers will be saved
  desktopPath: "./desktop/",

  // The path where the mobile wallpapers will be saved
  mobilePath: "./mobile/",

  // Width below which images will be discarded
  minWidth: 500,

  // Height below which images will be discarded
  minHeight: 500,

  // Automatically discards duplicate wallpapers after collecting new wallpapers
  autoRemoveDuplicates: true,

  // Move discarded wallpapers to a discard folder instead of removing them
  saveDiscarded: true,

  // The path where discarded wallpapers will be moved
  discardPath: "./discarded/"
}
```
