# :joystick: TUTORIEL :joystick: Comment fusionner vos axes de joysticks sur Joystick Gremlin `RC13.4.2+`

🇬🇧 The English version of this tutorial is available [here](https://github.com/Drakehinst/JoystickGremlin/blob/rc13.4/tutorials/tutorial_merge_axis_en.md)! 

:warning: **Attention !** :warning:

Ce tutoriel s'adresse aux utilisateurs des versions `RC13.4.2` et ultérieures. La fusion des axes de la version `RC13.4.1` ne fonctionnait pas avec 100% des périphériques et nécessitait un patch. Si néanmoins vous souhaitez consulter l'ancienne version de ce tutoriel, vous pour le trouver [au lien suivant](./tutorial_merge_axis_rc13.4.1_fr.md).

Si vous n'avez pas encore eu accès à un tutoriel qui voucre l'installation de Joystick Gremlin et de ma version patchée, commencez tout d'abord par suivre [mon tutoriel](https://docs.google.com/document/d/1I-leDLEKpazF2_WAtYluMx7QZ_VBB5Zp3lx3b7S7eOA/edit?usp=sharing), ou si vous préférez des vidéos explicatives, qui plus avec la partie configuration des touches et des axes, je vous recommande les vidéos tutoriel de Terada ([partie 1](https://www.youtube.com/watch?v=eNHzEOcrZ0o) et [partie 2](https://www.youtube.com/watch?v=AeQkpLXGKM4)). 😄

Et si vous rencontrez quelque problème que ce soit avec ma version patchée de Joystick Gremlin, le plus simple est de rejoindre le [serveur Discord HOTAS](https://discord.gg/hotas) et de me pinger @Drakehinst dans le [canal FAQ joystick-gremlin](https://discord.com/channels/438688364359581707/528501166385135636). Vu que toute conversation doit être faite en Anglais là-bas, si ce n'est pas votre tasse de thé vous pourrez me MP après avoir rejoint le serveur. 😉


## Étape 1

1. Téléchargez l'archive `joystick_gremlin_rc13.4.x.zip` de la version `RC13.4.2` ou ultérieure de Joystick Gremlin depuis [la page des Releases](https://github.com/Drakehinst/JoystickGremlin/releases).
1. Extrayez l'archive dans le dossier de votre choix.
1. Lancez `joystick_gremlin.exe` depuis le dossier principal.

![Fenêtre principale de Joystick Gremlin.](../images/tutorial_merge_axis/step_01.png)


## Étape 2

Vérifiez que la version de Joystick Gremlin est bien *"Release Candidate 13.4.2"* ou une version ultérieure dans le menu `Help / About`.

![Vérification de la version du logiciel dans l'onglet `Help/About`.](../images/tutorial_merge_axis/step_02_rc13.4.2.png)


## Étape 3

Chargez votre profil habituel puis vérifiez que tous vos périphériques sont détectés (joysticks, pédaliers, palonniers, clavier, vJoys, etc.).

![Indicateur que le profil est chargé dans la barre de titre de Joystick Gremlin, et liste des périphériques physiques et virtuels détectés.](../images/tutorial_merge_axis/step_03.png)


## Étape 4

Supprimez toutes les actions de type `Remap` sur les deux axes physiques à fusionner (ici *"T-Rudder - X Axis"* et *"T-Rudder - Y Axis"*). Par exemple, dans le profil ci-dessous, aucune action n'est associée à chacun des deux axes.

![Suppression de toute action de type `Remap` pour chacun des axes physiques à fusionner.](../images/tutorial_merge_axis/step_04.png)

:warning: **Attention !** :warning:

Selon leur configuration, les actions `Response Curve` peuvent fausser la fusion des axes. Si vous ne parvenez pas au résultat attendu à la fin de ce tutoriel, supprimez les `Response Curve` associées aux axes physiques que vous voulez fusionner et reconfigurez une unique `Response Curve` dans l'onglet du vJoy et à l'axe de sortie correspondants que vous aurez sélectionnés lors de la configuration du `Merge Axis`. 😉


## Étape 5

Configurez le "Merge Axis" comme dans l'exemple ci-dessous:
1. Ouvrez le menu `Action / Merge Axis`.
1. Cliquez sur `New Axis`.
1. L'axe *"Lower Half"* correspond à l'axe de marche arrière (par exemple la pédale de gauche).
1. L'axe *"Upper Half"* correspond à l'axe de marche avant (par exemple la pédale de droite).
1. Sélectionnez un axe de vJoy de sortie.
1. Sélectionnez l'opération de fusion `Average` (une sorte de Moyenne des axes, particulièrement adaptée à la fusion de la marche avant/arrière).
1. Ne modifiez **PAS ENCORE** les valeurs *"Initial value"*, elles le seront à l'[étape 8](../tutorials/tutorial_merge_axis_fr.md#étape-8).

![Configuration de la fusion des axes dans le menu `Action / Merge Axis`.](../images/tutorial_merge_axis/step_05_rc13.4.2.png)


## Étape 6

1. Fermez la fenêtre de `Merge Axis`.
1. Ouvrez l'outil `Tools / Input Viewer`.
1. Activez la visualisation des périphériques sur lesquels se situent les deux axes physiques que vous avez fusionnés à l'[étape 5](../tutorials/tutorial_merge_axis_fr.md#étape-5) (ici `T-Rudder / Axes - Current`, *"Axis 1"* et *"Axis 2"*, c'est-à-dire les axes X et Y), pour afficher leur diagramme de valeur en temps réel.

![Affichage de la valeur des axes physiques et virtuels, configurés précédemment dans `Merge Axis`, sur l'outil *"Tools / Input Viewer"*.](../images/tutorial_merge_axis/step_06.png)


## Étape 7

1. Appuyez à fond sur chacun des deux axes physiques (ici la pédale de gauche et la pédale de droite du *"T-Rudder"*, c'est-à-dire les axes X et Y, ou *"Axis 1"* et *"Axis 2"*)
1. Relâchez complètement les deux axes.
1. Notez la valeur de chacun des deux axes au repos, et divisez-la par 100 (par exemple: `100%` :arrow_right: `1.00`, `-100%` :arrow_right: `-1.00`, `0%` :arrow_right: `0.00`, `50%` :arrow_right: `0.50`).

![Affichage de la valeur des deux axes physiques quand ceux-ci sont complètement relâchés.](../images/tutorial_merge_axis/step_07.png)


## Étape 8

1. Minimisez la fenêtre du `Input Viewer` (nous y reviendrons pou le test final).
1. Ouvrez de nouveau la fenêtre de `Merge Axis`.
1. Entrez les valeur initiales (*"Initial value"*) trouvées à l'[étape 7](../tutorials/tutorial_merge_axis_fr.md#étape-7) dans les axes correspondants.
1. Fermez la fenêtre du `Merge Axis`.

![Réglage des valeurs initiales des axes fusionnés dans le menu `Merge Axis`](../images/tutorial_merge_axis/step_08_rc13.4.2.png)


## Étape 9

1. Sauvegardez votre profil (sous un autre nom s'il avait été créé avec une version antérieure de Joystick Gremlin, par sécurité).
1. Activez le profil.
1. Revenez à la fenêtre du `Input Viewer` et effectuez les vérifications suivantes:
    1. Activez la visualisation du *"vJoy Device"* dont vous avez sélectionné un axe comme l'axe de sortie du `Merge Axis` à l'[étape 5](../tutorials/tutorial_merge_axis_fr.md#étape-5) (ici `vJoy Device #1 / Axes - Current`, *"Axis1"*, c'est-à-dire l'axe X).
    1. Appuyez **à fond** sur l'axe de marche avant (par exemple la pédale de droite).
    1. Vérifiez que la valeur de l'axe du vJoy passe bien de `0%` à `100%` **(et non de `0%` à `50%`)**.
    1. Tout en maintenant le premier axe enfoncé, et appuyez **à fond** sur l'axe de marche arrière (par exemple la pédale de gauche).
    1. Vérifiez que la valeur de l'axe du vJoy passe bien de `100%` à `0%` **(et ne passe pas d'un coup de `50%` à `100%`, avant de diminuer jusqu'à `0%`, sinon vous devcrez vérifier de nouveau vos configurations à partir de l'[étape 5](../tutorials/tutorial_merge_axis_fr.md#étape-5))**.
    1. Relâchez **complètement** l'axe de marche avant.
    1. Vérifiez que la valeur de l'axe du vJoy passe bien de `0%` à `-100%`.
    
**:rocket: Si tout est fonctionnel, vous en avez terminé avec la configuration ! 😄**

---

:warning: **Attention !** :warning:

**À partir de maintenant, n'oubliez pas de toujours utiliser la version de Joystick Gremlin que vous avez téléchargéeet extraite à l'[étape 1](../tutorials/tutorial_merge_axis_fr.md#étape-1) !**

[La version 13 officielle](https://github.com/WhiteMagic/JoystickGremlin/releases) n'est plus développée par @WhiteMagic, le créateur de Joystick Gremlin, qui se consacre désormais au [développement de la version 14](https://github.com/WhiteMagic/JoystickGremlin/tree/develop).

En cas de doute, mettez à jour vos raccourcis pour les rediriger vers la version télechargée ici.

**Le profil que vous avez sauvegardé avec cette version est 100% rétro-compatible avec la version `13.3` officielle de Joystick Gremlin, mais si vous utilisez cette version plutôt que celle avec mon patch, le `Merge Axis` aura le comportement gênant décrit à l'[étape 9](../tutorials/tutorial_merge_axis_fr.md#étape-9). 😉**
