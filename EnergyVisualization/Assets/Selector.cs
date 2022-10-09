using System;
using UnityEngine;

public class Selector : MonoBehaviour
{
    private Camera cam;
    private IBuilding selection;

    public static event Action<IBuilding> OnSelect;

    private IBuilding Selection
    {
        set
        {
            selection.Deselect();
            selection = value;
            selection.Select();
            OnSelect.Invoke(selection);
        }
    }

    private void Awake()
    {
        cam = GetComponent<Camera>();
        selection = NullBuilding.Instance;

        // Register an empty event to avoid a NPE
        OnSelect += (building) => { };
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.Mouse0))
            Select();
    }

    private void Select()
    {
        RaycastHit hit;
        Ray ray = cam.ScreenPointToRay(Input.mousePosition);

        if (!Physics.Raycast(ray, out hit) || !hit.transform.TryGetComponent(out IBuilding building))
        {
            Selection = NullBuilding.Instance;
            return;
        }

        if (building == selection)
            Selection = NullBuilding.Instance;
        else
            Selection = building;
    }
}
