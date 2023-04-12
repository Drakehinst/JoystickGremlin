# **Changelog**

## **RC13.4.2 - 12/04/2023**

### **Contributors**

@Drakehinst

<!-- ### **Major changes** -->

### **Minor changes**

- The `Merge Axis` tool now contains fields for specifying the initial values of both physical axis. This replaces the solution implemented in version `RC13.4.2` (see Bugfixes for more details). The updated tutorial can be found at [the following link](/tutorials/tutorial_merge_axis_fr.md).

<!-- ### **Breaking changes** -->

### **Bugfixes**

- **The Merge Axis patch in version `RC13.4.1` (Issue #1) was not working for all device configurations:**
    - The initial physical axis values for several peripherals with more than 2 axis (e.g. Logitech G29 and Thrustmaster T3PA Pro) were not successfully configured via the dedicated fields in the Setting tab.
    - USB hubs may also have been a source of inconsistent indexing of the available physical axes.
    - This patch now implements a different solution: initial axis values are now set directly for both physical axes directly from the `Merge Axis` window.


## **RC13.4.1 - 21/02/2023**

### **Contributors**

@Drakehinst

<!-- ### **Major changes** -->

### **Minor changes**

- Changed requirement for vJoy version from `v2.1.8` to `v2.1.8 or later`

<!-- ### **Breaking changes** -->

### **Bugfixes**

- **Issue #1:**
    - Added support for initial axis values different from default 0.00 in the "Settings" tab
    - The custom initial axis values are saved in the profile XML, and are backwards compatible with R13.3_Debug
    - For a tutorial on how to use this new feature, please take a look at [this](./images/joystick_gremlin_rc13.4_how_to_merge_axis.png) (Available only in French for now)